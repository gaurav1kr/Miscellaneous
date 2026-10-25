# Safely Transfer Object Ownership Between Threads — C++11

## 60-second interview answer

Use `std::unique_ptr` for exclusive ownership. A producer moves the pointer to a worker using `std::move`; after the move, the producer's pointer is empty and the worker owns the object. For a continuous stream of tasks, pass `unique_ptr` objects through a queue protected by `std::mutex` and `std::condition_variable`. Synchronization safely publishes the task; ownership ensures its lifetime. Use `std::shared_ptr` only if concurrent ownership is genuinely required, and remember that it does not make the object itself thread-safe.

## Simple ownership flow

```mermaid
flowchart LR
  A[Producer: unique_ptr Task] -->|std::move| B[Thread-safe queue]
  B -->|std::move| C[Consumer: unique_ptr Task]
  C --> D[Task destroyed on scope exit]
```

## 1. Simplest working C++11 example

```cpp
#include <iostream>
#include <memory>
#include <thread>
#include <utility>

struct Task {
    int id;
    explicit Task(int n) : id(n) {}
    ~Task() { std::cout << "Task destroyed\n"; }
};

void worker(std::unique_ptr<Task> task) {
    std::cout << "Processing " << task->id << '\n';
}

int main() {
    std::unique_ptr<Task> task(new Task(100));
    std::thread t(worker, std::move(task));
    std::cout << "Producer still owns task: " << (task != nullptr) << '\n';
    t.join();
}
```

Compile: `g++ -std=c++11 -pthread -Wall -Wextra main.cpp -o app`

The print order between threads is nondeterministic. The moved-from `task` is empty.

## 2. Continuous workload: complete thread-safe queue example

```cpp
#include <condition_variable>
#include <iostream>
#include <memory>
#include <mutex>
#include <queue>
#include <thread>
#include <utility>

struct Task {
    int id;
    explicit Task(int n) : id(n) {}
};

class TaskQueue {
    std::queue<std::unique_ptr<Task>> tasks_;
    std::mutex mutex_;
    std::condition_variable cv_;
    bool stopped_ = false;

public:
    void push(std::unique_ptr<Task> task) {
        {
            std::lock_guard<std::mutex> lock(mutex_);
            if (stopped_) return; // task is destroyed safely
            tasks_.push(std::move(task));
        }
        cv_.notify_one();
    }

    bool pop(std::unique_ptr<Task>& result) {
        std::unique_lock<std::mutex> lock(mutex_);
        cv_.wait(lock, [this] { return stopped_ || !tasks_.empty(); });
        if (tasks_.empty()) return false;
        result = std::move(tasks_.front());
        tasks_.pop();
        return true;
    }

    void stop() {
        {
            std::lock_guard<std::mutex> lock(mutex_);
            stopped_ = true;
        }
        cv_.notify_all();
    }
};

int main() {
    TaskQueue queue;

    std::thread consumer([&queue] {
        std::unique_ptr<Task> task;
        while (queue.pop(task)) {
            std::cout << "Processed " << task->id << '\n';
            task.reset();
        }
    });

    for (int i = 1; i <= 3; ++i)
        queue.push(std::unique_ptr<Task>(new Task(i)));

    queue.stop();
    consumer.join();
}
```

`stop()` prevents new submissions but allows the consumer to drain queued tasks. Call `join()` before destroying the queue.

## 3. Why it is safe

- **Exclusive lifetime:** Only one `unique_ptr` owns a given task at a time.
- **Safe publication:** Mutex unlock/lock provides the required synchronization when handing a task through the queue.
- **No dangling owner:** The producer's `unique_ptr` becomes null after moving.
- **Short lock scope:** The consumer processes the task outside the queue mutex.
- **Clean shutdown:** The condition variable wakes the consumer and `join()` waits for it to finish.

## 4. Interview pitfalls

| Question | Short answer |
|---|---|
| Does `std::move` synchronize threads? | No. It permits moving; the thread or queue protocol provides synchronization. |
| Why not share a raw pointer? | Ownership and lifetime are unclear; it can dangle. |
| When use `shared_ptr`? | When several threads genuinely need concurrent ownership. |
| Does `shared_ptr` make `Task` thread-safe? | No; only ownership/reference counting is managed. |
| Can a moved-from `unique_ptr` be used? | It can be checked, reset, or reassigned; do not dereference it. |
| What if a worker throws? | Catch exceptions inside the thread; uncaught exceptions terminate the process. |
| Can the producer still access the task via a raw alias? | It must not access it concurrently without synchronization, and must not use it after destruction. |

## Whiteboard recall

**Create → move → synchronize publication → consume → destroy → join.**

`unique_ptr` solves ownership; `mutex` and `condition_variable` solve coordination.
