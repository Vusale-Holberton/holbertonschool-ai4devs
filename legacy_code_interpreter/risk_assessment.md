# Risk Assessment - Legacy Codebase

| Risk | Severity | Notes & Action Points |
| :--- | :--- | :--- |
| Hardcoded credentials | High | Found in config.php; exposes DB to unauthorized access. **Action:** Move credentials to environment variables (.env). |
| Missing unit tests | Medium | Untested critical modules increase regression risk. **Action:** Implement a testing framework like PHPUnit and cover core logic. |
| Deprecated API usage | High | Relies on removed PHP functions, leading to crashes. **Action:** Audit codebase and replace deprecated functions with modern equivalents. |
| Tight coupling | Medium | Modules are interdependent, making updates fragile. **Action:** Refactor code using Dependency Injection to decouple components. |
| Inadequate Error Logging | Medium | Lack of structured logs prevents tracking security breaches or system failures. **Action:** Integrate a logging library (e.g., Monolog) for real-time monitoring. |
| SQL Injection vulnerability | High | Unsanitized user inputs in legacy queries. **Action:** Use Prepared Statements and PDO for all database interactions to prevent data theft. |