# Risk Assessment - Legacy Codebase

| Risk | Severity | Notes |
| :--- | :--- | :--- |
| Hardcoded credentials | High | Found in config.php; exposes database passwords. Mitigation: Move to environment variables. |
| Missing unit tests | Medium | Critical modules untested; increases regression bug risk during refactoring. |
| Deprecated API usage | High | Relies on removed PHP functions; causes system crashes on newer server environments. |
| Tight coupling | Medium | Makes refactoring difficult; changes in one module break unrelated sections of the code. |
| No logging | Low | Debugging failures is nearly impossible; requires adding a centralized logging service like Monolog. |
| Lack of documentation | Medium | Onboarding new developers takes more time; increases the chance of introducing architectural errors. |
| SQL Injection vulnerability | High | Raw queries found in user inputs; poses a severe data breach risk. Mitigation: Use prepared statements. |
| Unsecured endpoints | High | Certain admin routes lack authentication; allows unauthorized access to sensitive data. |