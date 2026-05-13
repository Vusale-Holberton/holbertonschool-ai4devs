# Cross-Language Specification - Log Analyzer

## Algorithm
Parse server logs to extract meaningful insights and compute:
- Total number of requests
- Count of unique visitors (based on IP)
- Overall error rate (percentage of 4xx and 5xx status codes)

## Inputs
- Sample log files in standard Apache/Nginx format (text-based).

## Outputs
- A structured JSON object containing total_requests, unique_visitors, and error_rate.

## Edge Cases
- **Empty file:** Should return zero for all stats.
- **Malformed entry:** Skip lines that don't match the expected log format without crashing.
- **Large files:** Algorithm should process line-by-line to manage memory efficiency.

## Test Cases
- `log_small.txt` -> 100 requests, 20 errors, 15 unique IPs
- `log_empty.txt` -> 0 requests, 0 errors, 0 unique IPs
- `log_malformed.txt` -> 5 valid requests, 2 skipped malformed lines
- `log_all_errors.txt` -> 50 requests, 100% error rate
- `log_single_visitor.txt` -> 20 requests from 1 unique IP