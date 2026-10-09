#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <utility>
using namespace std;

class HttpRequest {
    string method_, url_, body_;
    map<string, string> headers_;
    int timeoutMs_, retries_;
public:
    HttpRequest(string method, string url, map<string,string> headers,
                string body, int timeoutMs, int retries)
        : method_(std::move(method)), url_(std::move(url)),
          body_(std::move(body)), headers_(std::move(headers)),
          timeoutMs_(timeoutMs), retries_(retries) {}

    void print() const {
        cout << method_ << " " << url_ << "\n";
        for (const auto& h : headers_)
            cout << h.first << ": " << h.second << "\n";
        cout << "Body: " << body_ << "\nTimeout: " << timeoutMs_
             << " ms\nRetries: " << retries_ << "\n";
    }
};

class HttpRequestBuilder {
    string method_ = "GET", url_, body_;
    map<string,string> headers_;
    int timeoutMs_ = 3000, retries_ = 0;
public:
    HttpRequestBuilder& setMethod(const string& value) {
        method_ = value; return *this;
    }
    HttpRequestBuilder& setURL(const string& value) {
        url_ = value; return *this;
    }
    HttpRequestBuilder& addHeader(const string& key, const string& value) {
        headers_[key] = value; return *this;
    }
    HttpRequestBuilder& setBody(const string& value) {
        body_ = value; return *this;
    }
    HttpRequestBuilder& setTimeout(int ms) {
        if (ms <= 0) throw invalid_argument("timeout must be positive");
        timeoutMs_ = ms; return *this;
    }
    HttpRequestBuilder& setRetries(int count) {
        if (count < 0) throw invalid_argument("retries cannot be negative");
        retries_ = count; return *this;
    }
    HttpRequest build() const {
        if (url_.empty()) throw invalid_argument("URL is required");
        if (method_.empty()) throw invalid_argument("method is required");
        return HttpRequest(method_, url_, headers_, body_, timeoutMs_, retries_);
    }
};

int main() {
    HttpRequest request = HttpRequestBuilder()
        .setMethod("POST")
        .setURL("/api/users")
        .addHeader("Content-Type", "application/json")
        .setBody(R"({"name":"Gaurav"})")
        .setTimeout(5000)
        .setRetries(3)
        .build();
    request.print();
}
