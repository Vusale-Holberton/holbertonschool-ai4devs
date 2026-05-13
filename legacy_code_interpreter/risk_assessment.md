# Risk Assessment - Legacy Codebase

| Risk | Severity | Notes |
| :--- | :--- | :--- |
| Hardcoded credentials | High | Found in config.php; leads to unauthorized database access and data breaches. |
| Missing unit tests | Medium | Critical modules untested; increases the risk of undetected bugs in production. |
| Deprecated API usage | High | Relies on removed PHP functions; will cause system crashes during server updates. |
| Tight coupling | Medium | Makes refactoring difficult; changes in one module may break unrelated features. |
| No logging | Low | Debugging failures is harder; delays response time to critical system errors. |
| SQL Injection vulnerability | High | User input not sanitized; allows attackers to steal or delete entire database records. |