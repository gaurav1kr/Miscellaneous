#include <algorithm>
#include <atomic>
#include <chrono>
#include <csignal>
#include <cstdlib>
#include <dirent.h>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <mutex>
#include <sstream>
#include <string>
#include <sys/statvfs.h>
#include <thread>
#include <unistd.h>
#include <vector>

struct Config {
    std::string flashPath = "/";
    int interval = 60;
    int cpuWindowShort = 60;
    int cpuWindowLong = 180;
    double daemonMB = 40, nativeMB = 110, webMB = 650;
    double cpuShortLimit = 95, cpuLongLimit = 90, flashLimit = 90;
    int cores = 4;
    bool actions = false;
    int iterations = 0; // zero means forever
};
struct Proc {
    pid_t pid = 0;
    unsigned long long starttime = 0;
    std::string name;
    double rssMB = 0;
    unsigned long long ticks = 0;
    unsigned long long writeBytes = 0;
};
struct CpuSample { std::chrono::steady_clock::time_point at; unsigned long long ticks; };
std::atomic<bool> running(true);
std::mutex ioMutex, registryMutex, historyMutex;
std::list<Proc> registry;
std::map<pid_t, std::vector<CpuSample>> history;
void log(const std::string &s) {
    std::lock_guard<std::mutex> lock(ioMutex);
    std::cout << s << std::endl;
}
void stopHandler(int) { running = false; }
bool digits(const char *s) {
    if (!*s) return false;
    for (; *s; ++s) if (*s < '0' || *s > '9') return false;
    return true;
}
std::string readName(pid_t pid) {
    std::ifstream f("/proc/" + std::to_string(pid) + "/comm");
    std::string name;
    std::getline(f, name);
    return name;
}
// /proc/PID/stat has a parenthesized comm field, which can contain spaces.
bool readStat(pid_t pid, unsigned long long &ticks, unsigned long long &start) {
    std::ifstream f("/proc/" + std::to_string(pid) + "/stat");
    std::string line;
    if (!std::getline(f, line)) return false;
    size_t close = line.rfind(')');
    if (close == std::string::npos || close + 2 >= line.size()) return false;
    std::istringstream ss(line.substr(close + 2));
    std::string field;
    unsigned long long utime = 0, stime = 0;
    // Remaining fields begin at #3 (state). utime=#14, stime=#15, starttime=#22.
    for (int i = 3; i <= 22; ++i) {
        if (!(ss >> field)) return false;
        try {
            if (i == 14) utime = std::stoull(field);
            if (i == 15) stime = std::stoull(field);
            if (i == 22) start = std::stoull(field);
        } catch (...) { return false; }
    }
    ticks = utime + stime;
    return true;
}
double readRSS(pid_t pid) {
    std::ifstream f("/proc/" + std::to_string(pid) + "/status");
    std::string key;
    long kb = 0;
    while (f >> key) {
        if (key == "VmRSS:") {
            if (f >> kb) return kb / 1024.0;
            break;
        }
        std::string rest;
        std::getline(f, rest);
    }
    return -1;
}
unsigned long long readWriteBytes(pid_t pid) {
    std::ifstream f("/proc/" + std::to_string(pid) + "/io");
    std::string key;
    unsigned long long value;
    while (f >> key >> value) if (key == "write_bytes:") return value;
    return 0;
}
std::vector<Proc> snapshot() {
    std::vector<Proc> v;
    DIR *dir = opendir("/proc");
    if (!dir) return v;
    struct dirent *e;
    while ((e = readdir(dir))) {
        if (!digits(e->d_name)) continue;
        Proc p;
        p.pid = static_cast<pid_t>(std::atoi(e->d_name));
        if (!readStat(p.pid, p.ticks, p.starttime)) continue;
        p.name = readName(p.pid);
        p.rssMB = readRSS(p.pid);
        p.writeBytes = readWriteBytes(p.pid);
        v.push_back(p);
    }
    closedir(dir);
    return v;
}
std::string category(const std::string &name) {
    // Demonstration classifier only; configure actual TV process names in production.
    if (name.find("Web") != std::string::npos || name.find("web") != std::string::npos ||
        name.find("chrome") != std::string::npos) return "web";
    if (name.find("App") != std::string::npos || name.find("app") != std::string::npos)
        return "native";
    return "daemon";
}
double limitFor(const Proc &p, const Config &c) {
    std::string type = category(p.name);
    return type == "web" ? c.webMB : type == "native" ? c.nativeMB : c.daemonMB;
}
void alarm(const std::string &type, const std::string &details) {
    log("ALARM [" + type + "] " + details + " | KPI/Splunk integration: mock event");
}
void memoryWorker(const Config &c) {
    int count = 0;
    while (running && (!c.iterations || count++ < c.iterations)) {
        std::vector<Proc> procs = snapshot();
        {
            std::lock_guard<std::mutex> lock(registryMutex);
            registry.assign(procs.begin(), procs.end()); // list tracks live PIDs; stale entries removed
        }
        for (const Proc &p : procs) {
            double lim = limitFor(p, c);
            if (p.rssMB >= 0 && p.rssMB >= lim) {
                std::ostringstream ss;
                ss << "pid=" << p.pid << " name=" << p.name << " RSS=" << p.rssMB
                   << "MiB threshold=" << lim << "MiB";
                alarm("MEMORY", ss.str());
                // SIGABRT (6 on Linux): disabled by default; only target validated identity.
                if (c.actions && p.pid != getpid()) {
                    unsigned long long ticks = 0, start = 0;
                    if (readStat(p.pid, ticks, start) && start == p.starttime) {
                        kill(p.pid, SIGABRT);
                    }
                }
            }
        }
        for (int i = 0; running && i < c.interval; ++i) std::this_thread::sleep_for(std::chrono::seconds(1));
    }
}
// CPU% convention: 100% means one fully utilized core, 400% means four cores.
// We sample each PID's accumulated utime+stime and compare against elapsed wall time.
void cpuWorker(const Config &c) {
    int count = 0;
    const long hz = sysconf(_SC_CLK_TCK);
    while (running && (!c.iterations || count++ < c.iterations)) {
        auto now = std::chrono::steady_clock::now();
        auto procs = snapshot();
        std::lock_guard<std::mutex> lock(historyMutex);
        for (const Proc &p : procs) {
            auto &samples = history[p.pid];
            // PID reuse protection: if ticks decrease, reset history.
            if (!samples.empty() && p.ticks < samples.back().ticks) samples.clear();
            samples.push_back({now, p.ticks});
            // Keep enough history for long window + one sampling interval.
            while (samples.size() > 2 &&
                std::chrono::duration<double>(now - samples[1].at).count() >
                c.cpuWindowLong + c.interval) samples.erase(samples.begin());
            for (int window : {c.cpuWindowShort, c.cpuWindowLong}) {
                // Select oldest sample no newer than window ago; need full window.
                const CpuSample *old = nullptr;
                for (const auto &s : samples) {
                    if (std::chrono::duration<double>(now - s.at).count() >= window) old = &s;
                    else break;
                }
                if (!old || hz <= 0 || p.ticks < old->ticks) continue;
                double secs = std::chrono::duration<double>(now - old->at).count();
                double cpu = 100.0 * (p.ticks - old->ticks) / (hz * secs);
                double limit = (window == c.cpuWindowShort ? c.cpuShortLimit : c.cpuLongLimit) * c.cores;
                if (cpu >= limit) {
                    std::ostringstream ss;
                    ss << "pid=" << p.pid << " name=" << p.name << " window=" << window
                       << "s CPU=" << std::fixed << std::setprecision(1) << cpu
                       << "% limit=" << limit << "% (per-core scale, max " << c.cores*100 << "%)";
                    alarm("CPU", ss.str());
                    // No kill here: demonstration avoids multiple worker races and PID reuse.
                }
            }
        }
        // Prune dead PIDs from history.
        std::map<pid_t, bool> alive;
        for (const auto &p : procs) alive[p.pid] = true;
        for (auto it = history.begin(); it != history.end(); ) {
            if (!alive.count(it->first)) it = history.erase(it); else ++it;
        }
        for (int i = 0; running && i < c.interval; ++i) std::this_thread::sleep_for(std::chrono::seconds(1));
    }
}
void flashWorker(const Config &c) {
    int count = 0;
    std::map<pid_t, std::pair<unsigned long long, unsigned long long>> previous;
    while (running && (!c.iterations || count++ < c.iterations)) {
        struct statvfs st;
        if (statvfs(c.flashPath.c_str(), &st) == 0 && st.f_blocks) {
            // f_bavail: free blocks available to unprivileged users.
            double used = 100.0 * (st.f_blocks - st.f_bavail) / st.f_blocks;
            log("FLASH path=" + c.flashPath + " used=" + std::to_string(used) + "%");
            auto procs = snapshot();
            std::vector<std::pair<unsigned long long, Proc>> writers;
            std::map<pid_t, std::pair<unsigned long long, unsigned long long>> current;
            for (const auto &p : procs) {
                auto it = previous.find(p.pid);
                unsigned long long delta = 0;
                if (it != previous.end() && it->second.first == p.starttime &&
                    p.writeBytes >= it->second.second)
                    delta = p.writeBytes - it->second.second;
                writers.push_back({delta, p});
                current[p.pid] = {p.starttime, p.writeBytes};
            }
            previous.swap(current);
            if (used >= c.flashLimit) {
                std::sort(writers.begin(), writers.end(), [](const auto &a, const auto &b) {
                    return a.first > b.first;
                });
                std::ostringstream ss;
                ss << "filesystem=" << c.flashPath << " used=" << used << "% top writers by write_bytes delta:";
                for (size_t i = 0; i < std::min<size_t>(5, writers.size()); ++i)
                    ss << " [pid=" << writers[i].second.pid << " " << writers[i].second.name
                       << " bytes=" << writers[i].first << "]";
                alarm("FLASH", ss.str());
                log("REBOOT REQUEST: simulated only; never rebooted by this sample");
            }
        } else log("FLASH: statvfs failed for " + c.flashPath);
        for (int i = 0; running && i < c.interval; ++i) std::this_thread::sleep_for(std::chrono::seconds(1));
    }
}
int main(int argc, char **argv) {
    Config c;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "--interval" && i+1 < argc) c.interval = std::atoi(argv[++i]);
        else if (arg == "--iterations" && i+1 < argc) c.iterations = std::atoi(argv[++i]);
        else if (arg == "--flash-path" && i+1 < argc) c.flashPath = argv[++i];
        else if (arg == "--cpu-short" && i+1 < argc) c.cpuWindowShort = std::atoi(argv[++i]);
        else if (arg == "--cpu-long" && i+1 < argc) c.cpuWindowLong = std::atoi(argv[++i]);
        else if (arg == "--enable-memory-sigabrt") c.actions = true;
        else { std::cerr << "Unknown or incomplete option: " << arg << '\n'; return 2; }
    }
    if (c.interval < 1 || c.cpuWindowShort < 1 || c.cpuWindowLong < c.cpuWindowShort || c.iterations < 0) {
        std::cerr << "Invalid configuration\n"; return 2;
    }
    std::signal(SIGINT, stopHandler);
    std::signal(SIGTERM, stopHandler);
    log("Starting 3 monitor threads; safe mode=" + std::string(c.actions ? "OFF (memory SIGABRT enabled)" : "ON"));
    std::thread mem(memoryWorker, std::cref(c));
    std::thread cpu(cpuWorker, std::cref(c));
    std::thread flash(flashWorker, std::cref(c));
    mem.join(); cpu.join(); flash.join();
    return 0;
}
