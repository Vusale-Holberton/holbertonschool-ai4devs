# Risk Assessment - Legacy Codebase

| Risk | Severity | Notes |
| :--- | :--- | :--- |
| Hardcoded credentials | High | Found in config.php; security vulnerability. |
| Missing unit tests | Medium | Critical modules untested; high regression risk. |
| Deprecated API usage | High | Relies on removed PHP functions; breakages expected. |
| Tight coupling | Medium | Low modularity makes refactoring difficult. |
| No logging | Low | Lack of execution logs makes debugging failures harder. |
| SQL Injection vulnerability | High | User input not sanitized in legacy database queries. |