# Adobe Senior Computer Scientist — C++ Comprehensive Interview Question Bank

**Scope:** Pointers, references, memory layout, `const`, constructors, destructors, copy/move semantics, ownership, polymorphism, undefined behavior, exception safety, and senior-level design.

**Practice standard:** Write implementation exercises in **C++11/C++14**. Later language features are identified as knowledge-only topics.

**How to use:** For each question, prepare (1) definition, (2) internal mechanics, (3) small compilable example, (4) edge cases/undefined behavior, (5) design trade-offs.

## Study progress

- [ ] 1. Pointers and pointer arithmetic (35)
- [ ] 2. References and value categories (25)
- [ ] 3. Memory layout and object lifetime (35)
- [ ] 4. `const`, `constexpr`, and qualifiers (25)
- [ ] 5. Constructors and initialization (30)
- [ ] 6. Destructors and lifetime (25)
- [ ] 7. Copy and move semantics (35)
- [ ] 8. Smart pointers and ownership (25)
- [ ] 9. Inheritance, polymorphism, and slicing (25)
- [ ] 10. Undefined behavior and code puzzles (25)
- [ ] 11. Exception safety and allocation (20)
- [ ] 12. Senior-level design scenarios (20)


## 1. Pointers and pointer arithmetic (35 questions)

1. What is a pointer? How is it different from a memory address?
2. What is the difference between `int* p`, `int** p`, and `int*** p`?
3. What is the size of a pointer on 32-bit and 64-bit systems?
4. Why does `sizeof(p)` differ from `sizeof(*p)`?
5. What is a null pointer? How does `nullptr` differ from `NULL` and `0`?
6. What happens when you dereference a null pointer?
7. What is a dangling pointer? How can you prevent it?
8. What is a wild or uninitialized pointer?
9. What is a `void*`? Can you dereference it directly?
10. Explain pointer arithmetic and how element size affects it.
11. Why does `p + 1` advance by `sizeof(*p)` bytes?
12. What happens if you increment a pointer beyond an array?
13. What is a one-past-the-end pointer, and when is it valid?
14. Can you subtract pointers belonging to different arrays?
15. What is pointer provenance, and why does it matter?
16. Explain `int const*`, `int* const`, and `int const* const`.
17. What is the difference between `char*`, `unsigned char*`, and `std::byte*`?
18. What are strict aliasing rules?
19. What is type punning? Why can `reinterpret_cast` be dangerous?
20. When should you use `static_cast`, `reinterpret_cast`, `const_cast`, and `dynamic_cast`?
21. What happens if you cast away `const` and modify a genuinely const object?
22. What is pointer alignment? What happens with a misaligned pointer?
23. Explain function pointers and pointers to member functions.
24. What is the difference between `T*` and `T(*)[N]`?
25. Why is `int**` not interchangeable with `const int**`?
26. Explain stack pointers versus pointers to dynamically allocated objects.
27. Why is returning the address of a local variable dangerous?
28. Can a pointer remain numerically unchanged but become invalid?
29. What is a use-after-free bug?
30. What is a double-free bug?
31. What is the ABA problem in lock-free programming?
32. How do pointers interact with placement `new`?
33. What is `std::launder`, and when is it needed?
34. What is the difference between an object pointer and an iterator?
35. How would you debug heap corruption caused by invalid pointer access?

## 2. References and value categories (25 questions)

1. What is a reference in C++?
2. How does a reference differ from a pointer?
3. Can a reference be null?
4. Can a reference be reseated after initialization?
5. Must a reference always be initialized?
6. Does a reference occupy memory?
7. What is the difference between `T&`, `const T&`, and `T&&`?
8. What is an lvalue?
9. What is an rvalue?
10. Explain glvalue, prvalue, and xvalue.
11. What is an rvalue reference?
12. Why were rvalue references introduced in C++11?
13. Can a non-const lvalue reference bind to a temporary?
14. How does `const T&` extend temporary lifetime?
15. What are the limitations of lifetime extension?
16. What happens when a function returns a reference to a local variable?
17. When should a function return by value versus reference?
18. What is reference collapsing?
19. Explain the four reference-collapsing combinations.
20. What is a forwarding reference?
21. What is perfect forwarding?
22. How does `std::forward` differ from `std::move`?
23. Why is a named rvalue-reference variable an lvalue expression?
24. What does `decltype(auto)` preserve that `auto` may not?
25. How can reference members affect assignment operators and object construction?

## 3. Memory layout and object lifetime (35 questions)

1. Explain the memory layout of a C++ process.
2. What are `.text`, `.data`, `.bss`, and `.rodata`?
3. Where are global variables stored?
4. Where are static local variables stored?
5. Where are string literals stored?
6. Where are dynamically allocated objects stored?
7. Where are member variables stored?
8. What is the difference between stack memory and heap memory?
9. What is virtual memory?
10. How does a virtual address translate to a physical address?
11. What are page tables and the TLB?
12. What happens during a page fault?
13. What is the difference between a segmentation fault and a stack overflow?
14. How is the stack size controlled on Linux and Windows?
15. What happens when a recursive function exhausts the stack?
16. What is memory alignment?
17. What are `alignof` and `alignas`?
18. What is structure padding?
19. How can member ordering reduce structure size?
20. What is `#pragma pack`, and what are its risks?
21. What is false sharing?
22. What is cache-line alignment?
23. What is the difference between `malloc`, `calloc`, `realloc`, and `new`?
24. Why must `malloc/free` not be mixed with `new/delete`?
25. What is the difference between allocation and object construction?
26. What is placement `new`?
27. How do you explicitly destroy a placement-constructed object?
28. What are object lifetime start and end rules?
29. What are storage duration and object lifetime, and how do they differ?
30. Explain automatic, static, thread, and dynamic storage duration.
31. What is thread-local storage?
32. What is the static initialization order fiasco?
33. What is the difference between zero-initialization and default-initialization?
34. What is ASLR?
35. How do you diagnose memory fragmentation and memory leaks?

## 4. const, constexpr, and qualifiers (25 questions)

1. What is `const` correctness?
2. Explain top-level and low-level `const`.
3. What is the difference between `const int*` and `int* const`?
4. What does `const` mean for a member function?
5. Can a const member function modify any members?
6. What is `mutable`?
7. When is `mutable` appropriate for synchronization?
8. Can you overload functions based on constness?
9. Why can `const T&` bind to a temporary?
10. What is the difference between `const` and `constexpr`?
11. What is `consteval`?
12. What is `constinit`?
13. Can a `constexpr` function execute at runtime?
14. What is a constant expression?
15. What is a literal type?
16. What is the difference between `constexpr` and macros?
17. What is `volatile`?
18. Why is `volatile` not a thread synchronization mechanism?
19. What is the difference between `std::atomic` and `volatile`?
20. Can you modify an object through `const_cast`?
21. How does `const` interact with smart pointers?
22. What is the difference between `const std::unique_ptr<T>` and `std::unique_ptr<const T>`?
23. What does `auto` discard or preserve regarding constness?
24. What is the difference between `auto`, `auto&`, and `const auto&`?
25. How do const-correct APIs improve maintainability and thread-safety reasoning?

## 5. Constructors and initialization (30 questions)

1. What is a constructor?
2. What is a default constructor?
3. What is a parameterized constructor?
4. What is a copy constructor?
5. What is a move constructor?
6. What is a converting constructor?
7. What is the purpose of `explicit`?
8. What is a delegating constructor?
9. What is an inherited constructor?
10. What is a `constexpr` constructor?
11. Can a constructor be virtual?
12. Can a constructor be static?
13. Can constructors be overloaded?
14. Can constructors throw exceptions?
15. What happens if a constructor throws halfway through?
16. In what order are base classes and members constructed?
17. Does the member initializer-list order control initialization order?
18. What happens when a member is omitted from the initializer list?
19. What is the difference between initialization and assignment?
20. Explain default-, value-, direct-, copy-, and list-initialization.
21. What is aggregate initialization?
22. What is `std::initializer_list` overload preference?
23. What is narrowing conversion during list-initialization?
24. What is the most vexing parse?
25. When is a default constructor implicitly deleted?
26. What does `= default` do?
27. What does `= delete` do?
28. Why should base constructors avoid calling virtual functions expecting derived dispatch?
29. What happens when a constructor publishes `this` before construction finishes?
30. How would you design a constructor for a class owning multiple resources with strong exception safety?

## 6. Destructors and lifetime (25 questions)

1. What is a destructor?
2. When is a destructor called?
3. Can a destructor be overloaded?
4. Can a destructor be virtual?
5. When must a base-class destructor be virtual?
6. Can a destructor be pure virtual?
7. Why must a pure virtual destructor still have a definition?
8. What happens when deleting a derived object through a base pointer without a virtual destructor?
9. What is destructor execution order?
10. What happens to members after the destructor body finishes?
11. What happens when a constructor throws—does that object's destructor run?
12. How are fully constructed members cleaned up after constructor failure?
13. What happens if a destructor throws during stack unwinding?
14. What is `std::terminate`?
15. What is the relationship between destructors and `noexcept`?
16. What is RAII?
17. Why is RAII central to exception-safe C++?
18. How do destructors release mutexes, file descriptors, and sockets?
19. What is the difference between `delete` and `delete[]`?
20. What is the difference between destroying an object and deallocating storage?
21. Can a destructor be explicitly invoked?
22. When is explicit destructor invocation valid?
23. What is the danger of manually invoking a destructor on an ordinary automatic object?
24. What happens when a destructor calls a virtual function?
25. What is the correct way to implement shutdown when cleanup can fail?

## 7. Copy and move semantics (35 questions)

1. What is shallow copying?
2. What is deep copying?
3. What is the difference between copy construction and copy assignment?
4. What is the Rule of Three?
5. What is the Rule of Five?
6. What is the Rule of Zero?
7. When does the compiler generate a copy constructor?
8. When is an implicit copy constructor deleted?
9. When is a move constructor implicitly generated?
10. What user-declared special members suppress implicit move generation?
11. What is a move constructor?
12. What is move assignment?
13. What is the purpose of `std::move`?
14. Does `std::move` actually move an object?
15. Why does `std::move` applied to a const object often result in copying?
16. What is a moved-from object's valid state?
17. What are self-assignment and self-move-assignment?
18. How should a copy assignment operator handle self-assignment?
19. What is the copy-and-swap idiom?
20. What are the tradeoffs of copy-and-swap?
21. What is copy elision?
22. What is NRVO?
23. What is guaranteed copy elision in C++17?
24. What is the difference between `return obj;` and `return std::move(obj);`?
25. Why can explicit `std::move` inhibit NRVO?
26. What is the importance of `noexcept` for move constructors?
27. How does `std::vector` behave during reallocation?
28. What is `std::move_if_noexcept`?
29. How do copy and move operations interact with inheritance?
30. What is object slicing?
31. How can you make a class non-copyable but movable?
32. How can you make a class neither copyable nor movable?
33. How would you implement a dynamic array with the Rule of Five?
34. How do exception guarantees influence copy assignment design?
35. Why should resource-owning classes generally prefer the Rule of Zero where possible?

## 8. Smart pointers and ownership (25 questions)

1. What problem do smart pointers solve?
2. How does `std::unique_ptr` work?
3. Why is `unique_ptr` move-only?
4. What is the difference between `make_unique` and direct `new`?
5. What is `std::shared_ptr`?
6. How does reference counting work?
7. What is the shared pointer control block?
8. What is the difference between `make_shared` and `shared_ptr(new T)`?
9. When is a shared object destroyed?
10. When is the control block destroyed?
11. What is `std::weak_ptr`?
12. How does `weak_ptr` prevent ownership cycles?
13. What happens when two shared objects own each other?
14. What is `enable_shared_from_this`?
15. Why is constructing a second `shared_ptr` from `this` dangerous?
16. What is the aliasing constructor of `shared_ptr`?
17. Are shared pointers thread-safe?
18. Is the pointed-to object automatically thread-safe?
19. What is a custom deleter?
20. How do you manage a `FILE*` or socket with RAII?
21. Can `unique_ptr` manage arrays?
22. What is the difference between `unique_ptr<T>` and `unique_ptr<T[]>`?
23. What are the performance costs of shared ownership?
24. When should you use a raw pointer as a non-owning observer?
25. How would you represent ownership across asynchronous callbacks?

## 9. Inheritance, polymorphism, and slicing (25 questions)

1. What is object slicing?
2. How do virtual functions work conceptually?
3. What is a vtable?
4. What is a vptr?
5. Are vtables and vptrs mandated by the C++ standard?
6. How does a virtual destructor affect object layout?
7. What is dynamic dispatch?
8. What is static dispatch?
9. What is the difference between overriding and overloading?
10. What does `override` enforce?
11. What does `final` enforce?
12. What is covariant return type?
13. What is a pure virtual function?
14. What is an abstract class?
15. What happens to virtual dispatch during construction and destruction?
16. How is multiple inheritance represented in memory?
17. What is the diamond inheritance problem?
18. How does virtual inheritance solve the diamond problem?
19. What is pointer adjustment in multiple inheritance?
20. How does `dynamic_cast` work conceptually?
21. What is RTTI?
22. What is the cost of virtual dispatch?
23. What is devirtualization?
24. What are object layout and ABI compatibility concerns?
25. How do you design an extensible polymorphic interface without accidental slicing or ownership ambiguity?

## 10. Undefined behavior and code puzzles (25 questions)

1. Dereferencing a null pointer.
2. Reading an uninitialized local variable.
3. Returning a pointer to a local array.
4. Returning a reference to a temporary with expired lifetime.
5. Using an iterator after vector reallocation.
6. Writing beyond a dynamically allocated array.
7. Calling `delete` twice on the same pointer.
8. Calling `delete[]` on memory allocated by scalar `new`.
9. Deleting a derived object through a non-virtual base destructor.
10. Accessing an object after its destructor has run.
11. Using `memcpy` on a non-trivially copyable resource-owning class.
12. Modifying a genuinely const object through `const_cast`.
13. Signed integer overflow.
14. Incorrectly reinterpreting object representation as another unrelated type.
15. Reading a union member other than the active member, outside permitted cases.
16. Modifying a container while iterating with invalidated iterators.
17. Concurrently modifying the same non-atomic variable.
18. Returning `std::move(local)` from a function.
19. Moving from a const `std::string`.
20. Passing a temporary to an API that stores its reference.
21. Initializing a reference member from a short-lived temporary.
22. Calling a virtual method in a base constructor.
23. Throwing from a destructor during stack unwinding.
24. Calling a pure virtual function during construction/destruction.
25. Reusing placement-new storage and accessing it through an invalid old pointer.

## 11. Exception safety and allocation (20 questions)

1. What is exception safety?
2. Explain no-throw, strong, and basic exception guarantees.
3. What is the difference between `new` failure and `malloc` failure?
4. What does `std::bad_alloc` mean?
5. What is `new (std::nothrow)`?
6. How do you override `operator new`?
7. How do you override `operator delete`?
8. What is the difference between allocation functions and `new` expressions?
9. What is sized deallocation?
10. What is aligned allocation?
11. What is a memory pool?
12. What is an arena allocator?
13. What is `std::pmr`?
14. How does an allocator influence container performance?
15. How can you implement an exception-safe constructor?
16. What happens if copying fails halfway through?
17. How can copy-and-swap provide the strong guarantee?
18. What happens when move construction throws during vector reallocation?
19. How can fault injection test exception safety?
20. How would you design memory allocation for a high-throughput, multithreaded C++ service?

## 12. Senior-level design scenarios (20 questions)

1. Design a thread-safe LRU cache. Explain ownership, lifetime, eviction, and iterator validity.
2. Design a memory pool for millions of small objects.
3. Implement a reference-counted smart pointer.
4. Implement a simplified `unique_ptr`.
5. Implement a vector-like dynamic array with exception safety.
6. Design a plugin interface that remains ABI-compatible across versions.
7. Diagnose a memory leak in a service that runs for weeks.
8. Debug a use-after-free that occurs only under heavy concurrency.
9. Explain why a C++ service's RSS remains high after freeing objects.
10. Design a safe callback-registration system where subscribers may be destroyed.
11. Implement a resource-owning wrapper around a Linux file descriptor.
12. Explain how to safely transfer object ownership between threads.
13. Optimize a large structure for cache locality.
14. Diagnose false sharing in a multithreaded workload.
15. Design an immutable configuration object shared across threads.
16. Implement an exception-safe class managing multiple resources.
17. Explain how to identify accidental deep copies in a hot path.
18. Design a high-performance producer-consumer queue and its lifetime model.
19. Diagnose heap corruption that disappears in debug builds.
20. Review a legacy C++ class and identify Rule-of-Five, lifetime, and undefined-behavior defects.

## 13. Must-practice coding exercises

| Exercise | Focus |
|---|---|
| Implement `String` | Deep copy, move, Rule of Five |
| Implement `Vector<T>` | Allocation, lifetime, exception safety |
| Implement `UniquePtr<T>` | RAII, move semantics |
| Implement `SharedPtr<T>` | Reference counting, control block |
| Implement thread-safe Singleton | Static lifetime, concurrency |
| Implement memory pool | Alignment, placement new |
| Implement LRU cache | Ownership, pointers, iterators |
| Implement polymorphic Shape hierarchy | Virtual destructors, slicing |
| Implement thread-safe object cache | Locks, lifetime, invalidation |
| Implement scoped file wrapper | RAII, ownership transfer |
| Implement circular buffer | Storage management, indexing |
| Implement callback registry | Dangling references, weak ownership |

## 14. Five code puzzles with explanations

### Puzzle 1 — Copy vs move (`std::move` on `const`)

```cpp
#include <iostream>
#include <utility>
class A {
public:
    A() { std::cout << "Default\n"; }
    A(const A&) { std::cout << "Copy\n"; }
    A(A&&) noexcept { std::cout << "Move\n"; }
};
int main() {
    A a;
    const A b;
    A c = std::move(a);
    A d = std::move(b);
}
```

**Output:** `Default`, `Default`, `Move`, `Copy` (each on its own line). `std::move(b)` is `const A&&`; it cannot bind to `A&&`, so copying occurs.

### Puzzle 2 — Construction/destruction order

```cpp
#include <iostream>
struct Base {
    Base() { std::cout << "Base ctor\n"; }
    virtual ~Base() { std::cout << "Base dtor\n"; }
};
struct Member {
    Member() { std::cout << "Member ctor\n"; }
    ~Member() { std::cout << "Member dtor\n"; }
};
struct Derived : Base {
    Member m;
    Derived() { std::cout << "Derived ctor\n"; }
    ~Derived() override { std::cout << "Derived dtor\n"; }
};
int main() { Derived d; }
```

**Output order:** Base ctor → Member ctor → Derived ctor → Derived dtor → Member dtor → Base dtor.

### Puzzle 3 — Dangling reference

```cpp
#include <string>
const std::string& getName() {
    return std::string("Adobe");
}
int main() {
    const std::string& name = getName();
}
```

**Explanation:** The function returns a dangling reference. Lifetime extension does not carry through a return statement. Do not read `name`; return `std::string` by value instead.

### Puzzle 4 — `sizeof` and padding

```cpp
#include <iostream>
struct A { char c; int i; char d; };
struct B { int i; char c; char d; };
int main() {
    std::cout << sizeof(A) << "\n";
    std::cout << sizeof(B) << "\n";
}
```

**Typical result:** `12` then `8` on a common ABI with four-byte `int` alignment. Exact sizes are implementation-dependent.

### Puzzle 5 — Missing virtual destructor

```cpp
#include <iostream>
class Base {
public:
    ~Base() { std::cout << "Base\n"; }
};
class Derived : public Base {
public:
    ~Derived() { std::cout << "Derived\n"; }
};
int main() {
    Base* p = new Derived();
    delete p;
}
```

**Explanation:** Undefined behavior. There is no guaranteed output. Fix with `virtual ~Base() = default;`.

## 15. Suggested seven-day revision schedule

| Day | Topics | Practical task |
|---|---|---|
| 1 | Pointers, arithmetic, aliasing, lifetime | Diagnose dangling pointers and UB |
| 2 | References, const, memory layout | Value-category and alignment puzzles |
| 3 | Constructors and destructors | Build an RAII resource wrapper |
| 4 | Copy/move semantics and exceptions | Implement `String` and `Vector<T>` |
| 5 | Smart pointers and ownership | Implement simplified `UniquePtr` |
| 6 | Polymorphism, object lifetime, design | Thread-safe LRU design review |
| 7 | Code puzzles and mock interview | Explain and debug five code samples |

## 16. Standards and interview notes

- Use `-std=c++11` or `-std=c++14` for implementation work; `std::make_unique` is C++14.
- `std::byte`, `std::launder`, guaranteed copy elision, and `std::pmr` are C++17 topics.
- `consteval` and `constinit` are C++20 topics.
- The precise vtable/vptr representation, structure sizes, and virtual-memory arrangement are not specified by the C++ language standard.
- In undefined-behavior questions, do not predict a guaranteed output.
- These are **questions and study prompts**, not complete model answers to every question.
