# Cross-Language Specification: Log Analyzer

## Overview
This specification defines a universal algorithm for analyzing server log files to extract key performance metrics.

## Algorithm Description
The analyzer must process a list of log strings and perform the following steps:
1. **Parsing**: Each line must be split into components. The IP address is expected at the beginning (index 0), and the HTTP status code is expected at index 8.
2. **Filtering**: Ignore any lines that do not follow the standard format or are empty.
3. **Calculation**:
    - **Total Requests**: Count all valid log entries.
    - **Unique Visitors**: Count the number of distinct IP addresses using a Set.
    - **Error Rate**: Calculate the percentage of requests where the status code is 400 or higher.

## Input Format
- A list of strings, where each string represents a single log entry in the Common Log Format.
- Example: `127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /index.html HTTP/1.0" 200 2326`

## Output Format
A dictionary/JSON object containing:
- `total_requests` (Integer)
- `unique_visitors` (Integer)
- `error_rate` (Float, rounded to 2 decimal places)

## Test Requirements
Implementations must pass at least 10 test cases, covering:
- Empty logs.
- Malformed log lines.
- Logs with 100% error rates.
- Logs with multiple requests from the same IP.