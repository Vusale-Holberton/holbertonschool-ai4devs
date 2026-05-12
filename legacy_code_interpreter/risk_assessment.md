# Risk Assessment - Legacy Codebase

| Risk | Severity | Notes |
| :--- | :--- | :--- |
| Hardcoded credentials | High | Found in config.php; security vulnerability |
| Missing unit tests | Medium | Critical modules untested; increases bug risk |
| Deprecated API usage | High | Relies on removed PHP functions; system instability |
| Tight coupling | Medium | Makes refactoring and scaling difficult |
| No logging | Low | Debugging failures and monitoring is harder |
| Lack of documentation | Medium | Onboarding new developers takes more time |