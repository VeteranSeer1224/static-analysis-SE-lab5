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
| **Missing function docstrings** | Pylint | All functions | Functions lacked descriptive docstrings explaining their purpose and arguments. | Added proper docstrings to all functions following PEP 257 conventions. | Low |

---

Reflection:
