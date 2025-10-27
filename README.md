# static-analysis-SE-lab5

# Static Code Analysis — Issue & Fix Documentation

## File: `inventory_system.py`

| **Issue Type** | **Tool Detected** | **Line(s)** | **Description** | **Fix Applied** | **Severity** |
|-----------------|------------------|--------------|------------------|------------------|---------------|
| **Missing module docstring** | Pylint | 1 | The file did not have a top-level description of its purpose. | Added a descriptive module-level docstring at the top of the file explaining functionality and best practices. | Low |
| **Mutable default argument** | Pylint | Function `addItem()` | Used `logs=[]` as a default parameter, which caused shared list references between calls. | Changed default to `logs=None` and initialized inside the function. | Medium |
| **Catching too general exception** | Pylint / Bandit | Function `removeItem()` | Used `except:` which catches all exceptions, potentially hiding bugs. | Replaced with specific `except KeyError` and `except TypeError` clauses. | High |
| **Use of global variable** | Pylint | Multiple functions (`loadData`, etc.) | Global variable `stock_data` was modified using `global` keyword, reducing modularity. | Replaced with explicit parameter passing — each function now receives and returns `stock_data`. | Medium |
| **Insecure function usage** | Bandit | Main block | Used `eval("print('eval used')")`, which is unsafe and can execute arbitrary code. | Removed `eval()` call entirely. | High |
| **Unsafe file handling** | Bandit / Pylint | `loadData()` and `saveData()` | Files were opened without context managers (`with`), risking unclosed files. | Updated both functions to use `with open()` syntax. | Medium |
| **Missing function docstrings** | Pylint | All functions | Functions lacked descriptive docstrings explaining their purpose and arguments. | Added proper docstrings to all functions. | Low |

---

Reflection:
# Reflection — Static Code Analysis and Fixes

## 1. What issues were identified by the static analysis tools?
The tools (Pylint, Bandit, and Flake8) identified several issues such as missing module and function docstrings, use of global variables, catching broad exceptions, mutable default arguments, and unsafe functions like `eval()`. Bandit also flagged insecure file handling practices.

---

## 2. How did you fix these issues?
I added proper module and function docstrings, replaced global variables with parameter passing, changed `except:` to specific exception types, removed unsafe functions, and implemented context managers (`with open()`) for file operations. I also corrected mutable default arguments and improved code readability.

---

## 3. What did you learn from this activity?
I learned the importance of writing secure, maintainable, and readable code. Static analysis tools help detect hidden issues early, improve software quality, and ensure compliance with best practices and secure coding guidelines.

---

## 4. How did the code quality improve after fixing the issues?
The Pylint score improved significantly, Bandit no longer reported security vulnerabilities, and Flake8 confirmed full style compliance. The code is now more modular, robust, and easier to maintain.

---

## 5. How can you apply these practices in future projects?
I will regularly run static analysis tools during development, write meaningful docstrings, handle exceptions carefully, and avoid using unsafe functions. This ensures better code quality, security, and long-term maintainability.

---
