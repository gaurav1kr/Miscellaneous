
# Task Scheduler Design and Implementation

## Low-Level Design (LLD)

### Components:
1. **Task**: Represents a unit of work with an abstract interface for executing tasks.
2. **TaskQueue**: A thread-safe queue to manage pending tasks.
3. **ThreadPool**: Manages a pool of threads that execute tasks from the task queue.
4. **TaskScheduler**: Orchestrates the thread pool and accepts new tasks for scheduling.

---

## Class Diagram
```
+-----------------+
|      Task       |  <- Abstract Base Class
+-----------------+
| + execute()     |
+-----------------+

           ^
           |
+-----------------+
| SpecificTask    |  <- Concrete Implementation
+-----------------+
| + execute()     |
+-----------------+

+-----------------+      +------------------+
|   TaskQueue     |      |   ThreadPool     |
+-----------------+      +------------------+
| + push(task)    |      | + start()        |
| + pop()         |      | + stop()         |
| + isEmpty()     |      | + enqueue(task)  |
+-----------------+      | + workerThread() |
                         +------------------+

                         +---------------------+
                         |   TaskScheduler     |
                         +---------------------+
                         | + schedule(task)    |
                         | + start()           |
                         | + stop()            |
                         +---------------------+
```

---

## C++ Implementation

### Task.h
```
#ifndef TASK_H
#define TASK_H

#include <iostream>

class Task 
{
public:
    virtual ~Task() = default;
    virtual void execute() = 0;
};

#endif // TASK_H
```

### SpecificTask.h
```
#ifndef SPECIFIC_TASK_H
#define SPECIFIC_TASK_H

#include "Task.h"

class SpecificTask : public Task 
{
    int id;

public:
    explicit SpecificTask(int taskId) : id(taskId) {}
    void execute() override 
    {
        std::cout << "Executing Task ID: " << id << std::endl;
    }
};

#endif // SPECIFIC_TASK_H
```

### TaskQueue.h
```
#ifndef TASK_QUEUE_H
#define TASK_QUEUE_H

#include <queue>
#include <mutex>
#include <condition_variable>
#include <memory>

class TaskQueue 
{
    std::queue<std::shared_ptr<Task>> queue;
    std::mutex mtx;
    std::condition_variable cv;

public:
    void push(std::shared_ptr<Task> task) 
    {
        std::lock_guard<std::mutex> lock(mtx);
        queue.push(task);
        cv.notify_one();
    }

    std::shared_ptr<Task> pop() 
    {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, [this] { return !queue.empty(); });
        auto task = queue.front();
        queue.pop();
        return task;
    }

    bool isEmpty() 
    {
        std::lock_guard<std::mutex> lock(mtx);
        return queue.empty();
    }
};

#endif // TASK_QUEUE_H
```

### ThreadPool.h
```
#ifndef THREAD_POOL_H
#define THREAD_POOL_H

#include "TaskQueue.h"
#include <thread>
#include <vector>
#include <atomic>

class ThreadPool 
{
    std::vector<std::thread> threads;
    TaskQueue &taskQueue;
    std::atomic<bool> running;

    void workerThread() 
    {
        while (running) 
	{
            auto task = taskQueue.pop();
            if (task) 
	    {
                task->execute();
            }
        }
    }

public:
    explicit ThreadPool(TaskQueue &queue, size_t threadCount = std::thread::hardware_concurrency())
        : taskQueue(queue), running(false) 
    {
        threads.reserve(threadCount);
    }

    void start() 
    {
        running = true;
        for (size_t i = 0; i < threads.capacity(); ++i) 
        {
            threads.emplace_back(&ThreadPool::workerThread, this);
        }
    }

    void stop() 
    {
        running = false;
        for (auto &thread : threads) 
	{
            if (thread.joinable()) 
	    {
                thread.join();
            }
        }
    }

    ~ThreadPool() 
    {
        stop();
    }
};

#endif // THREAD_POOL_H
```

### TaskScheduler.h
```
#ifndef TASK_SCHEDULER_H
#define TASK_SCHEDULER_H

#include "ThreadPool.h"
#include <memory>

class TaskScheduler 
{
    TaskQueue taskQueue;
    ThreadPool threadPool;

public:
    TaskScheduler() : threadPool(taskQueue) {}

    void start() 
    {
        threadPool.start();
    }

    void stop() 
    {
        threadPool.stop();
    }

    void schedule(std::shared_ptr<Task> task) 
    {
        taskQueue.push(task);
    }
};

#endif // TASK_SCHEDULER_H
```

### main.cpp
```
#include "TaskScheduler.h"
#include "SpecificTask.h"

int main() 
{
    TaskScheduler scheduler;

    scheduler.start();

    for (int i = 0; i < 10; ++i) 
    {
        scheduler.schedule(std::make_shared<SpecificTask>(i));
    }

    std::this_thread::sleep_for(std::chrono::seconds(2));
    scheduler.stop();

    return 0;
}
```

---

## Features of the Code
1. **Thread Pool**: Efficient reuse of threads.
2. **Thread-Safe Task Queue**: Ensures tasks are accessed safely across threads.
3. **Modular Design**: Each component is isolated for clarity and reusability.
4. **Modern C++ Concepts**:
   - **Smart Pointers**: Avoid manual memory management.
   - **Atomic Variables**: Ensure thread-safe state management.
   - **Condition Variables**: Facilitate thread synchronization.
5. **Scalable**: Thread pool size is determined dynamically.
