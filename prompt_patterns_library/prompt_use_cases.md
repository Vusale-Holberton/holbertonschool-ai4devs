# Prompt Use Cases

## 1. Code Quality & Refactoring

- **Code Optimization**
    - **Goal**: Improve execution speed and reduce complexity.
    - **Input**: Source code in [LANGUAGE].
    - **Output**: Optimized code with a brief performance explanation.
- **Legacy Code Modernization**
    - **Goal**: Update old syntax to modern standards (e.g., Python 2 to 3, ES5 to ES6).
    - **Input**: Deprecated code snippet.
    - **Output**: Modernized code using current best practices.
- **Naming Conventions Enforcement**
    - **Goal**: Ensure variables and functions follow a specific naming style (e.g., camelCase, snake_case).
    - **Input**: Code block with inconsistent naming.
    - **Output**: Refactored code with consistent naming.

## 2. Debugging & Error Handling

- **Stack Trace Analysis**
    - **Goal**: Identify the root cause of a crash based on logs.
    - **Input**: Error log and relevant source file.
    - **Output**: Explanation of the bug and a suggested fix.
- **Security Vulnerability Detection**
    - **Goal**: Find common security flaws like SQL Injection or XSS.
    - **Input**: Web application backend code.
    - **Output**: List of vulnerabilities and remediation steps.
- **Logical Bug Identification**
    - **Goal**: Find why a function returns the wrong value despite no syntax errors.
    - **Input**: Function code and expected vs. actual output.

## 3. Documentation & Learning

- **Automated API Documentation**
    - **Goal**: Generate documentation for public endpoints or classes.
    - **Input**: Undocumented source code.
    - **Output**: Structured documentation (Swagger/JSDoc style).
- **Complex Code Explanation**
    - **Goal**: Understand advanced algorithms or unfamiliar patterns.
    - **Input**: Complex code snippet.
    - **Output**: Line-by-line plain English explanation.

## 4. Testing & Quality Assurance

- **Unit Test Generation**
    - **Goal**: Increase code coverage with automated tests.
    - **Input**: Functional logic or method.
    - **Output**: Ready-to-run test cases using PyTest/Jest.
- **Edge Case Discovery**
    - **Goal**: Find scenarios where code might break.
    - **Input**: Function requirement description.
    - **Output**: List of boundary conditions and test values.