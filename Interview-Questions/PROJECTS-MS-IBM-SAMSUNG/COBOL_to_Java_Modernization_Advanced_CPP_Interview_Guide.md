# Legacy COBOL to Java Modernization Using Advanced C++

## Principal / Senior Principal Engineer Interview Design

> **Core design principle:** This is not a syntax-replacement problem.
> It is a **compiler/transpiler and semantic-preservation problem**. The
> generated Java must preserve the observable business behavior of the
> original COBOL application.

------------------------------------------------------------------------

## 1. Problem Statement

Assume an enterprise has a large legacy COBOL estate containing:

-   COBOL programs
-   COPYBOOKs
-   JCL/batch workflows
-   File processing
-   DB2 access
-   CICS integrations
-   Decades of business rules

The goal is to modernize selected COBOL workloads into maintainable Java
while preserving existing business behavior.

Example COBOL:

``` cobol
WORKING-STORAGE SECTION.
01 WS-BALANCE PIC 9(7)V99.
01 WS-AMOUNT  PIC 9(7)V99.

PROCEDURE DIVISION.

IF WS-BALANCE > WS-AMOUNT
    SUBTRACT WS-AMOUNT FROM WS-BALANCE
ELSE
    DISPLAY 'INSUFFICIENT BALANCE'
END-IF.
```

Possible Java:

``` java
if (balance.compareTo(amount) > 0) {
    balance = balance.subtract(amount);
} else {
    System.out.println("INSUFFICIENT BALANCE");
}
```

A direct text replacement approach is unsafe. For example, `PIC 9(7)V99`
represents fixed decimal semantics and should normally not be blindly
converted to a Java `double`.

The correct conceptual pipeline is:

``` text
COBOL source
    |
    v
Lexer / Parser
    |
    v
COBOL AST
    |
    v
Semantic Analysis
    |
    v
Language-Neutral IR
    |
    v
Transformation / Modernization Rules
    |
    v
Java Model / Java AST
    |
    v
Java Code Generation
    |
    v
Compilation + Differential Validation
```

------------------------------------------------------------------------

# 2. Functional Requirements

The modernization platform should:

1.  Read COBOL programs and related artifacts.
2.  Resolve COPYBOOK dependencies.
3.  Tokenize and parse COBOL syntax.
4.  Construct an Abstract Syntax Tree (AST).
5.  Build symbol tables and resolve variable types/scopes.
6.  Understand COBOL data declarations such as `PIC`, `COMP`, `COMP-3`,
    `OCCURS`, and `REDEFINES`.
7.  Analyze program control flow.
8.  Build a language-neutral Intermediate Representation (IR).
9.  Transform legacy constructs into structured target-language
    constructs.
10. Generate readable Java.
11. Preserve decimal, record, file, and transaction semantics.
12. Produce diagnostics for unsupported or ambiguous constructs.
13. Validate generated Java against the original COBOL behavior.
14. Support incremental migration instead of requiring a big-bang
    conversion.

------------------------------------------------------------------------

# 3. Non-Functional Requirements

### Correctness

Semantic equivalence is more important than simply generating compilable
Java.

### Scalability

The platform may need to analyze millions of lines of COBOL across
thousands of modules.

### Extensibility

New COBOL constructs and target-language transformations should be
addable without rewriting the complete engine.

### Maintainability

Parsing, semantic analysis, transformation, and code generation must
remain separate components.

### Performance

Avoid unnecessary copying of large AST/IR structures. Parallelize
independent modules where safe.

### Observability

Every warning/error should identify the file, line, transformation rule,
and reason.

### Recoverability

A single unsupported statement should not necessarily abort analysis of
an entire application.

------------------------------------------------------------------------

# 4. High-Level Design (HLD)

``` text
                   +-------------------------+
                   | Legacy Application      |
                   | COBOL / COPYBOOK / JCL |
                   +------------+------------+
                                |
                                v
                   +-------------------------+
                   | Source Manager          |
                   | Dependency Resolution   |
                   +------------+------------+
                                |
                                v
                   +-------------------------+
                   | Lexer                   |
                   | Tokenization            |
                   +------------+------------+
                                |
                                v
                   +-------------------------+
                   | Parser                  |
                   | COBOL Grammar           |
                   +------------+------------+
                                |
                                v
                   +-------------------------+
                   | COBOL AST               |
                   +------------+------------+
                                |
                                v
              +--------------------------------------+
              | Semantic Analysis                    |
              |--------------------------------------|
              | Symbol Table                         |
              | Type / Scope Resolution              |
              | Data Layout                          |
              | Control Flow / Call Graph            |
              +------------------+-------------------+
                                 |
                                 v
                    +--------------------------+
                    | Language-Neutral IR      |
                    +------------+-------------+
                                 |
                +----------------+----------------+
                |                                 |
                v                                 v
       +--------------------+          +----------------------+
       | Transformation     |          | Analysis Engine      |
       | Rules              |          | CFG / Call Graph     |
       | Modernization      |          | Dependency Graph     |
       +---------+----------+          +----------------------+
                 |
                 v
       +---------------------------+
       | Java Code Generator       |
       | Java Model / Pretty Print |
       +-------------+-------------+
                     |
                     v
              Generated Java
                     |
                     v
       +---------------------------+
       | Validation Engine         |
       |---------------------------|
       | Compile                   |
       | Unit Tests                |
       | Differential Testing      |
       | Regression Testing        |
       +---------------------------+
```

------------------------------------------------------------------------

# 5. Why an Intermediate Representation Is Important

Avoid tightly coupling the COBOL parser to Java:

``` text
COBOL AST -> Java
```

Prefer:

``` text
COBOL
  |
  v
COBOL AST
  |
  v
Semantic IR
  |
  +------------------+
  |                  |
  v                  v
Java Backend     Future Backend
                 e.g. C#/Kotlin
```

The AST represents the source program's syntax.

The IR represents the program's **meaning**.

Example:

``` cobol
ADD AMOUNT TO BALANCE
```

could become:

``` text
IRBinaryOperation
    operation = ADD
    source    = Variable(AMOUNT)
    target    = Variable(BALANCE)
```

The Java backend can then generate the appropriate Java expression based
on the resolved type.

For integer values:

``` java
balance += amount;
```

For decimal financial values:

``` java
balance = balance.add(amount);
```

This separation prevents Java-specific decisions from leaking into the
COBOL parser.

------------------------------------------------------------------------

# 6. Detailed Processing Approach

## Phase 1 - Inventory and Dependency Discovery

Before translating code, build an inventory of:

-   programs
-   COPYBOOKs
-   CALL relationships
-   JCL jobs
-   DB2 tables
-   CICS transactions
-   input/output files
-   external integrations

Example dependency graph:

``` text
PAYROLL-JOB
    |
    +--> PAYROLL-MAIN.cbl
            |
            +--> COPY EMPLOYEE-REC
            |
            +--> CALL TAX-CALC
            |
            +--> DB2 EMPLOYEE_TABLE
```

This graph helps determine migration boundaries and order.

------------------------------------------------------------------------

## Phase 2 - Source Normalization

Normalize source before semantic processing:

-   resolve COPY statements
-   normalize encoding where necessary
-   retain original source locations
-   identify dialect/compiler-specific extensions
-   preserve comments and source mappings where useful

Every generated construct should ideally be traceable back to its
original COBOL location.

------------------------------------------------------------------------

## Phase 3 - Lexical Analysis

Example:

``` cobol
IF BALANCE > AMOUNT
   SUBTRACT AMOUNT FROM BALANCE
END-IF
```

becomes approximately:

``` text
IF
IDENTIFIER(BALANCE)
GREATER_THAN
IDENTIFIER(AMOUNT)
SUBTRACT
IDENTIFIER(AMOUNT)
FROM
IDENTIFIER(BALANCE)
END_IF
```

C++:

``` cpp
enum class TokenType {
    Identifier,
    Number,
    StringLiteral,
    If,
    Else,
    EndIf,
    Move,
    Add,
    Subtract,
    From,
    To,
    Display,
    GreaterThan,
    EndOfFile
};
```

`enum class` gives strongly typed token values.

------------------------------------------------------------------------

# 7. AST Design

``` text
ASTNode
 |
 +-- Expression
 |     |
 |     +-- IdentifierExpression
 |     +-- LiteralExpression
 |     +-- BinaryExpression
 |
 +-- Statement
       |
       +-- MoveStatement
       +-- AddStatement
       +-- SubtractStatement
       +-- IfStatement
       +-- PerformStatement
       +-- DisplayStatement
       +-- CallStatement
```

Base interface:

``` cpp
class ASTNode {
public:
    virtual ~ASTNode() {}
    virtual void accept(ASTVisitor& visitor) const = 0;
};
```

The AST owns its children using `std::unique_ptr`.

``` cpp
class IfStatement : public Statement {
private:
    std::unique_ptr<Expression> condition_;
    std::vector<std::unique_ptr<Statement> > statements_;
};
```

This expresses ownership directly in the C++ type system.

------------------------------------------------------------------------

# 8. Visitor Pattern

Do not put Java generation, semantic validation, debugging output, and
dependency analysis inside every AST class.

Instead:

``` cpp
class ASTVisitor {
public:
    virtual ~ASTVisitor() {}

    virtual void visit(const IfStatement&) = 0;
    virtual void visit(const MoveStatement&) = 0;
    virtual void visit(const DisplayStatement&) = 0;
};
```

Visitors can include:

``` text
SemanticAnalyzer
IRBuilder
JavaGenerator
DependencyAnalyzer
DebugASTPrinter
ValidationVisitor
```

This keeps algorithms separate from the AST data model.

------------------------------------------------------------------------

# 9. Symbol Table and Semantic Analysis

Consider:

``` cobol
01 CUSTOMER-RECORD.
   05 CUSTOMER-ID      PIC 9(10).
   05 CUSTOMER-NAME    PIC X(30).
   05 ACCOUNT-BALANCE  PIC 9(10)V99.
```

Semantic information might become:

``` text
CUSTOMER-ID
    category  = Numeric
    precision = 10
    scale     = 0

CUSTOMER-NAME
    category  = Alphanumeric
    length    = 30

ACCOUNT-BALANCE
    category  = Decimal
    precision = 12
    scale     = 2
```

Possible C++ representation:

``` cpp
enum class DataType {
    Integer,
    Decimal,
    String,
    Boolean,
    Record,
    Array,
    PackedDecimal
};

struct Symbol {
    std::string name;
    DataType type;
    int precision;
    int scale;
};

class SymbolTable {
private:
    std::unordered_map<std::string, Symbol> symbols_;

public:
    void insert(const Symbol& symbol);
    const Symbol* lookup(const std::string& name) const;
};
```

`std::unordered_map` provides average O(1) lookup, which is useful
because symbol lookup occurs repeatedly during semantic analysis.

------------------------------------------------------------------------

# 10. COBOL to Java Type Mapping

A simplistic mapping is dangerous.

Potential mapping:

  -----------------------------------------------------------------------
  COBOL                   Semantic meaning        Possible Java
  ----------------------- ----------------------- -----------------------
  `PIC X(20)`             fixed-width             `String`
                          alphanumeric            

  `PIC 9(5)`              numeric integer         `int` / `long`

  `PIC S9(9)`             signed numeric          `int` / `long`

  `PIC 9(10)V99`          fixed decimal           `BigDecimal`

  `COMP-3`                packed decimal          `BigDecimal` or runtime
                                                  abstraction

  `OCCURS 10`             repeated structure      array / `List`

  group-level `01` record structured record       Java class

  `REDEFINES`             alternate storage view  special representation
                                                  / generated adapter
  -----------------------------------------------------------------------

The exact mapping depends on range, precision, storage semantics, and
usage.

------------------------------------------------------------------------

# 11. Biggest Probable Challenge I Faced

## Preserving COBOL Business Semantics While Mapping Legacy Data Representations to Java

A credible way to explain the hardest problem from my IBM modernization
exposure is:

> **The biggest challenge was not parsing COBOL syntax. It was
> preserving the semantics of legacy COBOL data and operations when
> representing them in a modern object-oriented language.**

COBOL applications frequently encode business rules in their data
representation.

For example:

``` cobol
01 ACCOUNT-BALANCE PIC S9(9)V99 COMP-3.
```

It would be easy to generate:

``` java
double accountBalance;
```

but that can introduce rounding differences.

For financial workloads, even a tiny numerical difference is
unacceptable.

A safer mapping may be:

``` java
BigDecimal accountBalance;
```

### Why this becomes difficult

The converter must consider:

1.  precision
2.  scale
3.  sign
4.  storage format
5.  rounding rules
6.  overflow behavior
7.  truncation behavior
8.  comparison semantics
9.  initialization/default values
10. interactions with other fields

`REDEFINES` makes the problem harder.

Example:

``` cobol
01 RAW-DATA       PIC X(10).
01 NUMERIC-DATA REDEFINES RAW-DATA PIC 9(10).
```

The same bytes can be interpreted through different logical views.

Java does not naturally have the same memory-layout model.

### Design solution

I would avoid resolving these cases directly in the parser.

Instead:

``` text
COBOL declaration
       |
       v
AST declaration
       |
       v
Semantic Type Resolver
       |
       v
Canonical IR Type
       |
       v
Target Type Strategy
       |
       v
Java representation
```

The IR retains enough semantic metadata:

``` text
DecimalType
    precision = 11
    scale = 2
    signed = true
    storage = PACKED_DECIMAL
```

The Java backend then decides how to represent it.

### How I would describe this in the interview

> "One of the biggest challenges I encountered in the modernization area
> was that syntactically simple COBOL constructs could carry very
> specific data semantics. Decimal and packed-decimal fields are a good
> example. A naive conversion to Java primitive floating-point types
> could produce a program that compiles and appears correct but gives
> subtly different financial results. The approach was therefore to
> preserve source-language type metadata during analysis and make
> target-type selection a semantic transformation rather than a parser
> decision. That separation also made the transformation engine easier
> to extend and validate."

### Why this is a strong challenge to discuss

It lets the interviewer drill into:

-   C++ class design
-   data representation
-   floating-point vs fixed decimal
-   compiler architecture
-   Strategy Pattern
-   testing
-   correctness
-   enterprise migration risk

It is also much stronger than saying "the parser was difficult."

------------------------------------------------------------------------

# 12. Other Difficult COBOL Constructs

Expect questions around:

``` text
COPYBOOK resolution
PIC clauses
COMP / COMP-3
REDEFINES
OCCURS
OCCURS DEPENDING ON
PERFORM
GO TO
paragraph fall-through
file status semantics
EBCDIC / encoding
CICS
DB2 embedded SQL
JCL dependencies
CALL between programs
global/shared state
decimal arithmetic
record layouts
transaction boundaries
```

Parsing these constructs is only the first step. Their runtime behavior
must also be preserved.

------------------------------------------------------------------------

# 13. Control Flow Graph

Legacy COBOL can contain control flow that does not map directly to
structured Java.

Construct a CFG:

``` text
              Entry
                |
                v
             Block A
                |
             Condition
             /       \
          true       false
           |           |
           v           v
        Block B     Block C
           \           /
            \         /
             v       v
              Block D
                |
                v
               Exit
```

A CFG helps analyze:

-   branches
-   loops
-   `PERFORM`
-   `GO TO`
-   unreachable code
-   paragraph fall-through
-   opportunities to reconstruct structured control flow

------------------------------------------------------------------------

# 14. Advanced C++ Features and Their Role

  -------------------------------------------------------------------------
  C++ feature                         Usage
  ----------------------------------- -------------------------------------
  RAII                                deterministic cleanup of files,
                                      parser resources, AST/IR objects

  `std::unique_ptr`                   single ownership of AST and IR
                                      children

  `std::shared_ptr`                   genuinely shared immutable metadata
                                      where necessary

  `std::weak_ptr`                     avoid ownership cycles in shared
                                      graphs

  move semantics                      transfer large AST/IR structures
                                      without deep copies

  polymorphism                        AST/IR node hierarchy

  virtual destructor                  correct destruction through base
                                      pointers

  Visitor Pattern                     semantic analysis and code generation

  Strategy Pattern                    pluggable conversion rules

  Factory Pattern                     centralized AST/IR construction

  templates                           reusable type-safe utilities and
                                      traversals

  `enum class`                        tokens, operators, semantic types

  STL containers                      vectors, maps, symbol tables,
                                      dependency graphs

  `const` correctness                 protect semantic models from
                                      accidental modification

  exceptions                          fatal parser/infrastructure failures
                                      where appropriate

  thread primitives                   parallel module analysis

  lambdas                             local
                                      transformations/filtering/traversal
                                      helpers
  -------------------------------------------------------------------------

For interview coding, keep the implementation C++11/14 compatible.

------------------------------------------------------------------------

# 15. Why `unique_ptr` Is a Natural AST Choice

Consider:

``` text
IfStatement
    |
    +-- condition
    |
    +-- thenStatement
    |
    +-- elseStatement
```

Each child normally has exactly one owning parent.

Therefore:

``` cpp
std::unique_ptr<Expression>
std::unique_ptr<Statement>
```

is a natural ownership model.

Benefits:

-   no manual `delete`
-   clear ownership
-   automatic cleanup
-   exception safety
-   fewer memory leaks
-   move-only semantics prevent accidental ownership copying

A good interview statement:

> **I prefer encoding ownership in the type system rather than relying
> on comments or developer convention.**

------------------------------------------------------------------------

# 16. Move Semantics

Large AST/IR trees should not be repeatedly copied.

``` cpp
std::unique_ptr<Program> Parser::parse();
```

Ownership can be transferred using:

``` cpp
std::move(node)
```

For containers:

``` cpp
Program(std::vector<std::unique_ptr<Statement> >&& statements)
    : statements_(std::move(statements)) {
}
```

This is particularly useful when processing large source bases.

------------------------------------------------------------------------

# 17. Strategy Pattern for Transformation Rules

``` cpp
class TransformationRule {
public:
    virtual ~TransformationRule() {}

    virtual bool matches(const ASTNode& node) const = 0;

    virtual std::unique_ptr<IRNode>
    transform(const ASTNode& node) const = 0;
};
```

Possible implementations:

``` text
MoveTransformation
ArithmeticTransformation
PerformTransformation
RecordTransformation
FileIOTransformation
CallTransformation
DecimalTransformation
```

This makes individual modernization rules independently testable and
replaceable.

------------------------------------------------------------------------

# 18. Diagnostics

Do not return only:

``` text
Translation failed.
```

Use structured diagnostics:

``` cpp
enum class Severity {
    Info,
    Warning,
    Error,
    Fatal
};

struct Diagnostic {
    Severity severity;
    std::string file;
    int line;
    int column;
    std::string code;
    std::string message;
};
```

Example:

``` text
COB00127
CUSTOMER.cbl:421
Warning: REDEFINES requires manual semantic verification.
```

At application level:

``` text
96.8% automatically translated
 2.4% translated with warnings
 0.8% requires manual remediation
```

This is much more practical for enterprise modernization.

------------------------------------------------------------------------

# 19. Parallel Processing

Thousands of independent COBOL modules can potentially be parsed in
parallel.

``` text
                  Work Queue
                     |
       +-------------+-------------+
       |             |             |
       v             v             v
    Worker 1      Worker 2      Worker 3
       |             |             |
       v             v             v
     AST/IR        AST/IR        AST/IR
```

Prefer:

``` text
immutable shared configuration
+
per-module parser/AST/semantic state
+
carefully controlled shared dependency metadata
```

over a giant global data structure protected by one mutex.

C++11 facilities include:

``` cpp
std::thread
std::mutex
std::lock_guard
std::condition_variable
std::future
std::async
```

The goal is not "use threads everywhere"; the goal is to identify safe
module-level parallelism while avoiding lock contention.

------------------------------------------------------------------------

# 20. Validation Strategy

The most important question is not:

> Did the converter generate Java?

It is:

> **Does the Java behave like the COBOL?**

Use differential testing:

``` text
                   Test Input
                       |
             +---------+---------+
             |                   |
             v                   v
       Original COBOL      Generated Java
             |                   |
             v                   v
        Output A             Output B
             \                   /
              \                 /
               +-------+-------+
                       |
                       v
                    Compare
                       |
              +--------+--------+
              |                 |
            Match            Difference
```

Compare observable effects:

-   output records
-   financial calculations
-   database updates
-   generated files
-   status/error codes
-   business decisions
-   transaction results

For critical modules, consider shadow execution before cutover.

------------------------------------------------------------------------

# 21. Incremental Migration Strategy

Avoid a big-bang migration.

``` text
Application Inventory
        |
        v
Dependency Analysis
        |
        v
Choose Bounded Module
        |
        v
Convert to Java
        |
        v
Compile + Static Checks
        |
        v
Differential Tests
        |
        v
Shadow / Parallel Run
        |
        v
Controlled Cutover
        |
        v
Next Module
```

Adapters can temporarily allow Java and COBOL modules to coexist.

------------------------------------------------------------------------

# 22. LLD - Main Classes

``` text
+-------------------------+
| SourceManager           |
+-------------------------+
| loadProgram()           |
| resolveCopybook()       |
+------------+------------+
             |
             v
+-------------------------+
| Lexer                   |
+-------------------------+
| tokenize()              |
+------------+------------+
             |
             v
+-------------------------+
| Parser                  |
+-------------------------+
| parseProgram()          |
| parseStatement()        |
| parseExpression()       |
+------------+------------+
             |
             v
+-------------------------+
| ASTNode                 |
+-------------------------+
             |
       +-----+------+
       |            |
  Expression     Statement
                    |
        +-----------+-----------+
        |           |           |
       If         Move       Display
             |
             v
+-------------------------+
| SemanticAnalyzer        |
+-------------------------+
| SymbolTable             |
| TypeResolver            |
| ScopeResolver           |
+------------+------------+
             |
             v
+-------------------------+
| IRBuilder               |
+-------------------------+
| build()                 |
+------------+------------+
             |
             v
+-------------------------+
| IRProgram               |
+-------------------------+
             |
      +------+------+
      |             |
      v             v
+-----------+  +-----------+
| CFGBuilder|  | Optimizer |
+-----------+  +-----------+
      \             /
       \           /
        v         v
     +---------------+
     | JavaGenerator |
     +---------------+
             |
             v
        Java Source
```

------------------------------------------------------------------------

# 23. Working C++11/14 Mini Transpiler

The following is intentionally a **small working demonstration**, not a
complete COBOL compiler.

It demonstrates:

-   Lexer
-   token representation
-   recursive-descent Parser
-   AST hierarchy
-   `std::unique_ptr`
-   move semantics
-   polymorphism
-   virtual destructors
-   Visitor Pattern
-   symbol normalization
-   Java generation
-   error handling

Supported mini-language:

``` cobol
MOVE 100 TO BALANCE
DISPLAY BALANCE
IF BALANCE > 50
    DISPLAY 'SUFFICIENT BALANCE'
ELSE
    DISPLAY 'INSUFFICIENT BALANCE'
END-IF
```

## `cobol_to_java.cpp`

``` cpp
#include <cctype>
#include <iostream>
#include <memory>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

// ------------------------------------------------------------
// Token Model
// ------------------------------------------------------------

enum class TokenType {
    Identifier,
    Number,
    StringLiteral,

    Move,
    To,
    Display,

    If,
    Else,
    EndIf,

    GreaterThan,

    EndOfFile
};

struct Token {
    TokenType type;
    std::string text;
    int line;

    Token(TokenType t, const std::string& value, int ln)
        : type(t), text(value), line(ln) {
    }
};

// ------------------------------------------------------------
// Lexer
// ------------------------------------------------------------

class Lexer {
private:
    std::string input_;
    std::size_t pos_;
    int line_;

    char current() const {
        if (pos_ >= input_.size()) {
            return '\0';
        }
        return input_[pos_];
    }

    char peek(std::size_t offset = 1) const {
        std::size_t p = pos_ + offset;
        if (p >= input_.size()) {
            return '\0';
        }
        return input_[p];
    }

    void advance() {
        if (current() == '\n') {
            ++line_;
        }

        if (pos_ < input_.size()) {
            ++pos_;
        }
    }

    void skipWhitespace() {
        while (std::isspace(static_cast<unsigned char>(current()))) {
            advance();
        }
    }

    static std::string toUpper(std::string value) {
        for (std::size_t i = 0; i < value.size(); ++i) {
            value[i] = static_cast<char>(
                std::toupper(static_cast<unsigned char>(value[i])));
        }
        return value;
    }

    Token identifierOrKeyword() {
        const int tokenLine = line_;
        std::string value;

        while (std::isalnum(static_cast<unsigned char>(current())) ||
               current() == '-' ||
               current() == '_') {
            value += current();
            advance();
        }

        const std::string upper = toUpper(value);

        if (upper == "MOVE") {
            return Token(TokenType::Move, value, tokenLine);
        }
        if (upper == "TO") {
            return Token(TokenType::To, value, tokenLine);
        }
        if (upper == "DISPLAY") {
            return Token(TokenType::Display, value, tokenLine);
        }
        if (upper == "IF") {
            return Token(TokenType::If, value, tokenLine);
        }
        if (upper == "ELSE") {
            return Token(TokenType::Else, value, tokenLine);
        }
        if (upper == "END-IF") {
            return Token(TokenType::EndIf, value, tokenLine);
        }

        return Token(TokenType::Identifier, value, tokenLine);
    }

    Token number() {
        const int tokenLine = line_;
        std::string value;

        while (std::isdigit(static_cast<unsigned char>(current())) ||
               current() == '.') {
            value += current();
            advance();
        }

        return Token(TokenType::Number, value, tokenLine);
    }

    Token stringLiteral() {
        const int tokenLine = line_;
        const char quote = current();

        advance();

        std::string value;

        while (current() != '\0' && current() != quote) {
            value += current();
            advance();
        }

        if (current() != quote) {
            throw std::runtime_error(
                "Unterminated string literal at line " +
                std::to_string(tokenLine));
        }

        advance();

        return Token(TokenType::StringLiteral, value, tokenLine);
    }

public:
    explicit Lexer(const std::string& input)
        : input_(input), pos_(0), line_(1) {
    }

    std::vector<Token> tokenize() {
        std::vector<Token> tokens;

        while (true) {
            skipWhitespace();

            if (current() == '\0') {
                tokens.push_back(
                    Token(TokenType::EndOfFile, "", line_));
                break;
            }

            if (std::isalpha(static_cast<unsigned char>(current())) ||
                current() == '_') {
                tokens.push_back(identifierOrKeyword());
                continue;
            }

            if (std::isdigit(static_cast<unsigned char>(current()))) {
                tokens.push_back(number());
                continue;
            }

            if (current() == '\'' || current() == '"') {
                tokens.push_back(stringLiteral());
                continue;
            }

            if (current() == '>') {
                tokens.push_back(
                    Token(TokenType::GreaterThan, ">", line_));
                advance();
                continue;
            }

            std::ostringstream message;
            message << "Unexpected character '" << current()
                    << "' at line " << line_;

            throw std::runtime_error(message.str());
        }

        return tokens;
    }
};

// ------------------------------------------------------------
// Forward declarations for Visitor
// ------------------------------------------------------------

class NumberExpression;
class IdentifierExpression;
class StringExpression;
class BinaryExpression;

class MoveStatement;
class DisplayStatement;
class IfStatement;

class ASTVisitor {
public:
    virtual ~ASTVisitor() {}

    virtual void visit(const NumberExpression& node) = 0;
    virtual void visit(const IdentifierExpression& node) = 0;
    virtual void visit(const StringExpression& node) = 0;
    virtual void visit(const BinaryExpression& node) = 0;

    virtual void visit(const MoveStatement& node) = 0;
    virtual void visit(const DisplayStatement& node) = 0;
    virtual void visit(const IfStatement& node) = 0;
};

// ------------------------------------------------------------
// AST Base Classes
// ------------------------------------------------------------

class ASTNode {
public:
    virtual ~ASTNode() {}
    virtual void accept(ASTVisitor& visitor) const = 0;
};

class Expression : public ASTNode {
public:
    virtual ~Expression() {}
};

class Statement : public ASTNode {
public:
    virtual ~Statement() {}
};

// ------------------------------------------------------------
// Expression Nodes
// ------------------------------------------------------------

class NumberExpression : public Expression {
private:
    std::string value_;

public:
    explicit NumberExpression(const std::string& value)
        : value_(value) {
    }

    const std::string& value() const {
        return value_;
    }

    void accept(ASTVisitor& visitor) const override {
        visitor.visit(*this);
    }
};

class IdentifierExpression : public Expression {
private:
    std::string name_;

public:
    explicit IdentifierExpression(const std::string& name)
        : name_(name) {
    }

    const std::string& name() const {
        return name_;
    }

    void accept(ASTVisitor& visitor) const override {
        visitor.visit(*this);
    }
};

class StringExpression : public Expression {
private:
    std::string value_;

public:
    explicit StringExpression(const std::string& value)
        : value_(value) {
    }

    const std::string& value() const {
        return value_;
    }

    void accept(ASTVisitor& visitor) const override {
        visitor.visit(*this);
    }
};

enum class BinaryOperator {
    GreaterThan
};

class BinaryExpression : public Expression {
private:
    BinaryOperator op_;
    std::unique_ptr<Expression> left_;
    std::unique_ptr<Expression> right_;

public:
    BinaryExpression(BinaryOperator op,
                     std::unique_ptr<Expression> left,
                     std::unique_ptr<Expression> right)
        : op_(op),
          left_(std::move(left)),
          right_(std::move(right)) {
    }

    BinaryOperator op() const {
        return op_;
    }

    const Expression& left() const {
        return *left_;
    }

    const Expression& right() const {
        return *right_;
    }

    void accept(ASTVisitor& visitor) const override {
        visitor.visit(*this);
    }
};

// ------------------------------------------------------------
// Statement Nodes
// ------------------------------------------------------------

class MoveStatement : public Statement {
private:
    std::unique_ptr<Expression> source_;
    std::string destination_;

public:
    MoveStatement(std::unique_ptr<Expression> source,
                  const std::string& destination)
        : source_(std::move(source)),
          destination_(destination) {
    }

    const Expression& source() const {
        return *source_;
    }

    const std::string& destination() const {
        return destination_;
    }

    void accept(ASTVisitor& visitor) const override {
        visitor.visit(*this);
    }
};

class DisplayStatement : public Statement {
private:
    std::unique_ptr<Expression> expression_;

public:
    explicit DisplayStatement(std::unique_ptr<Expression> expression)
        : expression_(std::move(expression)) {
    }

    const Expression& expression() const {
        return *expression_;
    }

    void accept(ASTVisitor& visitor) const override {
        visitor.visit(*this);
    }
};

class IfStatement : public Statement {
private:
    std::unique_ptr<Expression> condition_;
    std::vector<std::unique_ptr<Statement> > thenStatements_;
    std::vector<std::unique_ptr<Statement> > elseStatements_;

public:
    IfStatement(
        std::unique_ptr<Expression> condition,
        std::vector<std::unique_ptr<Statement> > thenStatements,
        std::vector<std::unique_ptr<Statement> > elseStatements)
        : condition_(std::move(condition)),
          thenStatements_(std::move(thenStatements)),
          elseStatements_(std::move(elseStatements)) {
    }

    const Expression& condition() const {
        return *condition_;
    }

    const std::vector<std::unique_ptr<Statement> >&
    thenStatements() const {
        return thenStatements_;
    }

    const std::vector<std::unique_ptr<Statement> >&
    elseStatements() const {
        return elseStatements_;
    }

    void accept(ASTVisitor& visitor) const override {
        visitor.visit(*this);
    }
};

class Program {
private:
    std::vector<std::unique_ptr<Statement> > statements_;

public:
    explicit Program(
        std::vector<std::unique_ptr<Statement> > statements)
        : statements_(std::move(statements)) {
    }

    const std::vector<std::unique_ptr<Statement> >&
    statements() const {
        return statements_;
    }
};

// ------------------------------------------------------------
// Recursive-Descent Parser
// ------------------------------------------------------------

class Parser {
private:
    std::vector<Token> tokens_;
    std::size_t pos_;

    const Token& current() const {
        return tokens_[pos_];
    }

    bool check(TokenType type) const {
        return current().type == type;
    }

    const Token& consume(TokenType expected,
                         const std::string& message) {
        if (!check(expected)) {
            std::ostringstream out;
            out << message
                << " at line " << current().line
                << ". Found token: " << current().text;

            throw std::runtime_error(out.str());
        }

        return tokens_[pos_++];
    }

    std::unique_ptr<Expression> parsePrimary() {
        if (check(TokenType::Number)) {
            std::string value =
                consume(TokenType::Number,
                        "Expected number").text;

            return std::unique_ptr<Expression>(
                new NumberExpression(value));
        }

        if (check(TokenType::StringLiteral)) {
            std::string value =
                consume(TokenType::StringLiteral,
                        "Expected string").text;

            return std::unique_ptr<Expression>(
                new StringExpression(value));
        }

        if (check(TokenType::Identifier)) {
            std::string name =
                consume(TokenType::Identifier,
                        "Expected identifier").text;

            return std::unique_ptr<Expression>(
                new IdentifierExpression(name));
        }

        throw std::runtime_error(
            "Expected expression at line " +
            std::to_string(current().line));
    }

    std::unique_ptr<Expression> parseCondition() {
        std::unique_ptr<Expression> left = parsePrimary();

        consume(TokenType::GreaterThan,
                "Expected '>' in IF condition");

        std::unique_ptr<Expression> right = parsePrimary();

        return std::unique_ptr<Expression>(
            new BinaryExpression(
                BinaryOperator::GreaterThan,
                std::move(left),
                std::move(right)));
    }

    std::unique_ptr<Statement> parseMove() {
        consume(TokenType::Move, "Expected MOVE");

        std::unique_ptr<Expression> source = parsePrimary();

        consume(TokenType::To, "Expected TO after MOVE value");

        const std::string destination =
            consume(TokenType::Identifier,
                    "Expected destination identifier").text;

        return std::unique_ptr<Statement>(
            new MoveStatement(
                std::move(source),
                destination));
    }

    std::unique_ptr<Statement> parseDisplay() {
        consume(TokenType::Display, "Expected DISPLAY");

        std::unique_ptr<Expression> expression = parsePrimary();

        return std::unique_ptr<Statement>(
            new DisplayStatement(std::move(expression)));
    }

    std::unique_ptr<Statement> parseIf() {
        consume(TokenType::If, "Expected IF");

        std::unique_ptr<Expression> condition =
            parseCondition();

        std::vector<std::unique_ptr<Statement> > thenStatements;
        std::vector<std::unique_ptr<Statement> > elseStatements;

        while (!check(TokenType::Else) &&
               !check(TokenType::EndIf) &&
               !check(TokenType::EndOfFile)) {
            thenStatements.push_back(parseStatement());
        }

        if (check(TokenType::Else)) {
            consume(TokenType::Else, "Expected ELSE");

            while (!check(TokenType::EndIf) &&
                   !check(TokenType::EndOfFile)) {
                elseStatements.push_back(parseStatement());
            }
        }

        consume(TokenType::EndIf,
                "Expected END-IF");

        return std::unique_ptr<Statement>(
            new IfStatement(
                std::move(condition),
                std::move(thenStatements),
                std::move(elseStatements)));
    }

    std::unique_ptr<Statement> parseStatement() {
        if (check(TokenType::Move)) {
            return parseMove();
        }

        if (check(TokenType::Display)) {
            return parseDisplay();
        }

        if (check(TokenType::If)) {
            return parseIf();
        }

        std::ostringstream out;
        out << "Unsupported statement at line "
            << current().line
            << ": " << current().text;

        throw std::runtime_error(out.str());
    }

public:
    explicit Parser(std::vector<Token> tokens)
        : tokens_(std::move(tokens)), pos_(0) {
    }

    Program parseProgram() {
        std::vector<std::unique_ptr<Statement> > statements;

        while (!check(TokenType::EndOfFile)) {
            statements.push_back(parseStatement());
        }

        return Program(std::move(statements));
    }
};

// ------------------------------------------------------------
// Java Code Generator Visitor
// ------------------------------------------------------------

class JavaGenerator : public ASTVisitor {
private:
    std::ostringstream output_;
    int indent_;

    void writeIndent() {
        for (int i = 0; i < indent_; ++i) {
            output_ << "    ";
        }
    }

    static std::string normalizeIdentifier(
        const std::string& cobolName) {

        std::string result;
        bool uppercaseNext = false;

        for (std::size_t i = 0; i < cobolName.size(); ++i) {
            char c = cobolName[i];

            if (c == '-' || c == '_') {
                uppercaseNext = true;
                continue;
            }

            if (result.empty()) {
                result += static_cast<char>(
                    std::tolower(
                        static_cast<unsigned char>(c)));
                uppercaseNext = false;
                continue;
            }

            if (uppercaseNext) {
                result += static_cast<char>(
                    std::toupper(
                        static_cast<unsigned char>(c)));
                uppercaseNext = false;
            } else {
                result += static_cast<char>(
                    std::tolower(
                        static_cast<unsigned char>(c)));
            }
        }

        return result;
    }

    static std::string escapeJavaString(
        const std::string& value) {

        std::string result;

        for (std::size_t i = 0; i < value.size(); ++i) {
            const char c = value[i];

            if (c == '\\') {
                result += "\\\\";
            } else if (c == '"') {
                result += "\\\"";
            } else if (c == '\n') {
                result += "\\n";
            } else {
                result += c;
            }
        }

        return result;
    }

public:
    JavaGenerator()
        : indent_(0) {
    }

    std::string generate(const Program& program) {
        output_ << "public class GeneratedProgram {\n";
        ++indent_;

        writeIndent();
        output_ << "public static void main(String[] args) {\n";
        ++indent_;

        // In a production implementation these declarations would come
        // from semantic analysis / a symbol table rather than being
        // hard-coded.
        writeIndent();
        output_ << "double balance = 0;\n\n";

        const std::vector<std::unique_ptr<Statement> >& statements =
            program.statements();

        for (std::size_t i = 0; i < statements.size(); ++i) {
            statements[i]->accept(*this);
        }

        --indent_;
        writeIndent();
        output_ << "}\n";

        --indent_;
        output_ << "}\n";

        return output_.str();
    }

    void visit(const NumberExpression& node) override {
        output_ << node.value();
    }

    void visit(const IdentifierExpression& node) override {
        output_ << normalizeIdentifier(node.name());
    }

    void visit(const StringExpression& node) override {
        output_ << "\""
                << escapeJavaString(node.value())
                << "\"";
    }

    void visit(const BinaryExpression& node) override {
        output_ << "(";
        node.left().accept(*this);

        switch (node.op()) {
            case BinaryOperator::GreaterThan:
                output_ << " > ";
                break;
        }

        node.right().accept(*this);
        output_ << ")";
    }

    void visit(const MoveStatement& node) override {
        writeIndent();

        output_ << normalizeIdentifier(node.destination())
                << " = ";

        node.source().accept(*this);

        output_ << ";\n";
    }

    void visit(const DisplayStatement& node) override {
        writeIndent();
        output_ << "System.out.println(";
        node.expression().accept(*this);
        output_ << ");\n";
    }

    void visit(const IfStatement& node) override {
        writeIndent();
        output_ << "if ";

        node.condition().accept(*this);

        output_ << " {\n";

        ++indent_;

        const std::vector<std::unique_ptr<Statement> >& thenPart =
            node.thenStatements();

        for (std::size_t i = 0; i < thenPart.size(); ++i) {
            thenPart[i]->accept(*this);
        }

        --indent_;
        writeIndent();
        output_ << "}";

        const std::vector<std::unique_ptr<Statement> >& elsePart =
            node.elseStatements();

        if (!elsePart.empty()) {
            output_ << " else {\n";

            ++indent_;

            for (std::size_t i = 0; i < elsePart.size(); ++i) {
                elsePart[i]->accept(*this);
            }

            --indent_;
            writeIndent();
            output_ << "}";
        }

        output_ << "\n";
    }
};

// ------------------------------------------------------------
// Demo
// ------------------------------------------------------------

int main() {
    try {
        const std::string cobol =
            "MOVE 100 TO BALANCE\n"
            "DISPLAY BALANCE\n"
            "IF BALANCE > 50\n"
            "    DISPLAY 'SUFFICIENT BALANCE'\n"
            "ELSE\n"
            "    DISPLAY 'INSUFFICIENT BALANCE'\n"
            "END-IF\n";

        std::cout << "===== INPUT COBOL =====\n";
        std::cout << cobol << "\n";

        Lexer lexer(cobol);
        std::vector<Token> tokens = lexer.tokenize();

        Parser parser(std::move(tokens));
        Program program = parser.parseProgram();

        JavaGenerator generator;
        const std::string javaCode =
            generator.generate(program);

        std::cout << "===== GENERATED JAVA =====\n";
        std::cout << javaCode << "\n";

        return 0;
    }
    catch (const std::exception& ex) {
        std::cerr << "Translation failed: "
                  << ex.what() << "\n";

        return 1;
    }
}
```

------------------------------------------------------------------------

# 24. Compile and Run

Linux/macOS with a C++14 compiler:

``` bash
g++ -std=c++14 -Wall -Wextra -pedantic cobol_to_java.cpp -o cobol_to_java
./cobol_to_java
```

The generated Java will be approximately:

``` java
public class GeneratedProgram {
    public static void main(String[] args) {
        double balance = 0;

        balance = 100;
        System.out.println(balance);
        if (balance > 50) {
            System.out.println("SUFFICIENT BALANCE");
        } else {
            System.out.println("INSUFFICIENT BALANCE");
        }
    }
}
```

For the production architecture described earlier, the hard-coded
`double balance` declaration would **not** be used. The type would be
determined by semantic analysis. A COBOL fixed-decimal field could
instead result in `BigDecimal`.

------------------------------------------------------------------------

# 25. How the Demo Maps to Advanced C++

## RAII

All AST memory is automatically released when its owning object goes out
of scope.

No explicit `delete` is required.

## `unique_ptr`

``` cpp
std::unique_ptr<Expression>
std::unique_ptr<Statement>
```

models exclusive ownership.

## Move Semantics

``` cpp
std::move(source)
std::move(condition)
std::move(tokens)
```

transfers ownership without deep copying.

## Polymorphism

``` cpp
Expression
Statement
```

are abstract concepts with concrete derived classes.

## Virtual Destructor

``` cpp
virtual ~ASTNode() {}
```

allows safe destruction through base-class pointers.

## Visitor Pattern

``` cpp
node.accept(generator);
```

dispatches to:

``` cpp
visit(const MoveStatement&)
visit(const DisplayStatement&)
visit(const IfStatement&)
```

without embedding Java-generation behavior inside the AST classes.

## STL

The design uses:

``` cpp
std::vector
std::string
std::unique_ptr
std::ostringstream
```

A full implementation would also naturally use:

``` cpp
std::unordered_map
std::unordered_set
std::queue
std::stack
```

for symbol tables and graph algorithms.

------------------------------------------------------------------------

# 26. Production Version vs Demo

The demo intentionally simplifies several things.

A production engine would add:

``` text
SourceManager
    |
    +-- COBOL source
    +-- COPYBOOK resolver
    +-- source location tracking

Lexer
    |
Parser
    |
COBOL AST
    |
Semantic Analyzer
    |
    +-- SymbolTable
    +-- TypeResolver
    +-- ScopeResolver
    +-- RecordLayoutAnalyzer
    |
IR Builder
    |
Canonical IR
    |
    +-- CFG Builder
    +-- Call Graph
    +-- Transformation Rules
    |
Java Model
    |
Java Generator
    |
Formatter
    |
Compiler
    |
Differential Test Engine
```

The demo generates `double` only to keep the example executable and
understandable. A production implementation must resolve actual COBOL
type semantics before choosing a Java type.

------------------------------------------------------------------------

# 27. How I Would Explain My IBM Experience

Avoid implying ownership of the complete compiler if the actual
contribution was limited to a part of the system.

A good answer:

> "At IBM I worked in an application-modernization area where a
> C++-based core was involved in COBOL-to-Java transformation. My direct
> contribution was to part of that system rather than owning the entire
> compiler pipeline. That exposure gave me an understanding of the kinds
> of problems such a modernization engine has to solve. If I were
> designing the platform end-to-end, I would structure it like a
> compiler: source ingestion and COPYBOOK resolution, parsing into an
> AST, semantic analysis, a language-neutral IR, transformation passes,
> Java generation, and finally differential validation."

Continue with:

> "The architectural boundary I consider particularly important is the
> IR. I would not let the COBOL parser directly generate Java because
> that couples source-language parsing to target-language decisions and
> makes difficult semantic cases much harder to manage."

------------------------------------------------------------------------

# 28. Principal Engineer Discussion Points

At Principal level, move the discussion beyond classes.

Talk about:

### Migration risk

What if generated Java compiles but changes financial behavior?

### Blast radius

Which downstream applications consume the generated files/database
records?

### Dependency graph

Can this module actually be migrated independently?

### Rollback

How do we revert if shadow execution finds a mismatch?

### Observability

Can we trace a generated Java statement back to the COBOL source?

### Extensibility

Can new COBOL dialects and transformation rules be added safely?

### Performance

Can independent modules be analyzed concurrently?

### Maintainability

Will engineers maintain generated Java, or will COBOL remain the source
of truth?

That last question affects the entire architecture.

------------------------------------------------------------------------

# 29. Probable Follow-Up Interview Questions

### Why not use regex?

Regex can assist with localized preprocessing, but it cannot reliably
represent nested grammar, scopes, type semantics, control flow, and
cross-file dependencies. A parser/AST is required for robust
transformation.

### Why AST + IR? Why not only AST?

AST represents source syntax. IR represents semantic operations in a
target-independent form. The IR decouples the COBOL frontend from Java
generation and gives us a stable layer for optimization and analysis.

### Why `unique_ptr` instead of `shared_ptr` everywhere?

AST ownership is normally hierarchical. `unique_ptr` makes ownership
explicit, avoids reference-count overhead, and prevents accidental
shared ownership. `shared_ptr` should only be introduced when the domain
genuinely requires shared lifetime.

### Where would `weak_ptr` be useful?

If graph objects use shared ownership and contain back-references,
`weak_ptr` can prevent reference cycles. For many compiler graphs,
non-owning IDs/references may be even simpler.

### Why Visitor Pattern?

It lets multiple operations traverse the same AST without putting every
operation into every AST node.

### Why `BigDecimal`?

COBOL business applications often depend on fixed decimal behavior.
Binary floating point can introduce rounding differences that are
unacceptable for financial calculations.

### How would you handle unsupported COBOL?

Emit structured diagnostics, retain source location, classify the issue
as warning/error/manual remediation, and continue analyzing independent
units where possible.

### How would you verify correctness?

Differential testing: execute COBOL and generated Java using the same
input and compare observable output and side effects.

### Would you migrate everything at once?

No. Build dependencies, identify bounded domains/modules, convert
incrementally, validate, shadow-run where appropriate, cut over, and
retain rollback.

### How would you scale to thousands of programs?

Parallelize independent module parsing/analysis, minimize shared mutable
state, cache resolved COPYBOOKs/metadata, and build dependency-aware
work scheduling.

------------------------------------------------------------------------

# 30. Two-Minute Interview Answer

> "I would treat COBOL-to-Java modernization as a compiler and
> semantic-preservation problem rather than a text-conversion problem.
>
> I would first inventory COBOL programs, COPYBOOKs, calls, JCL, DB2 and
> other dependencies. The frontend would tokenize and parse COBOL into
> an AST. A semantic-analysis stage would then build symbol tables,
> resolve scopes and types, understand COBOL data layouts, and construct
> control-flow information.
>
> I would transform that AST into a language-neutral IR. That is an
> important architectural boundary because COBOL and Java have very
> different data and execution models. The IR captures what the program
> means rather than how the COBOL was written.
>
> A Java backend would convert the IR into Java constructs. For example,
> fixed-decimal COBOL financial fields might map to BigDecimal rather
> than double so that we don't silently change business behavior.
>
> In C++, I would use RAII and unique_ptr for AST/IR ownership, move
> semantics to avoid unnecessary copies, STL containers for symbol
> tables and dependency graphs, polymorphism for AST nodes, Visitor for
> semantic analysis and code generation, and Strategy-style
> transformation rules for individual COBOL constructs.
>
> The biggest challenge is semantic preservation, especially data
> representation and legacy control flow. Therefore the final stage is
> not simply compilation. I would use differential testing: run the
> original COBOL and generated Java with identical inputs and compare
> outputs, database changes, files, status codes and business decisions.
>
> At application scale, I would construct dependency graphs and migrate
> bounded modules incrementally rather than doing a big-bang
> conversion."

------------------------------------------------------------------------

# 31. Whiteboard Version to Remember

``` text
 COBOL + COPYBOOK + JCL
            |
            v
      Source Manager
            |
            v
       Lexer/Parser
            |
            v
           AST
            |
            v
   Semantic Analysis
 Type + Scope + Symbols
            |
            v
    Language-Neutral IR
            |
            v
 Transformation Rules
            |
            v
      Java Generator
            |
            v
           Java
            |
            v
 Differential Validation
            |
            v
 Incremental Production
        Migration
```

------------------------------------------------------------------------

# 32. Five Lines to Remember

If time is short, remember these:

1.  **"This is a semantic-preservation problem, not a string-replacement
    problem."**
2.  **"I would separate the COBOL frontend from Java generation through
    a language-neutral IR."**
3.  **"I would encode AST/IR ownership using RAII and `unique_ptr`, and
    use move semantics for efficient ownership transfer."**
4.  **"The hardest problem is preserving COBOL data and runtime
    semantics, especially decimal types, record layouts, REDEFINES, and
    legacy control flow."**
5.  **"Success means behavioral equivalence verified through
    differential testing---not merely that the generated Java
    compiles."**

------------------------------------------------------------------------

## Final Interview Positioning

The strongest way to position the project is:

``` text
Not:

"I converted COBOL syntax into Java."

Instead:

"I worked in a legacy application-modernization area involving a
C++-based transformation core. The engineering problem is essentially
compiler design plus semantic preservation: parse the legacy language,
build semantic representations, transform them safely, generate modern
code, and prove behavioral equivalence."
```

That framing naturally opens discussion into advanced C++, compiler
design, distributed processing, testing, architecture, migration
strategy, and Principal-level engineering trade-offs.
