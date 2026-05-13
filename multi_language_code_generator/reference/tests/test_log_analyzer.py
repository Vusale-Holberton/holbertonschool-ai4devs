import unittest
from reference.log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_empty_log(self):
        self.assertEqual(self.analyzer.analyze([])["total_requests"], 0)

    def test_single_valid_request(self):
        log = ['127.0.0.1 - - [10/May/2026] "GET / HTTP/1.1" 200 512']
        res = self.analyzer.analyze(log)
        self.assertEqual(res["total_requests"], 1)
        self.assertEqual(res["error_rate"], 0.0)

    def test_error_counting(self):
        log = ['127.0.0.1 - - [10/May] "GET /" 404 123']
        self.assertEqual(self.analyzer.analyze(log)["error_rate"], 100.0)

    def test_unique_visitors(self):
        log = [
            '192.168.1.1 - - "GET /" 200 123',
            '192.168.1.1 - - "GET /" 200 123',
            '192.168.1.2 - - "GET /" 200 123'
        ]
        self.assertEqual(self.analyzer.analyze(log)["unique_visitors"], 2)

    def test_malformed_line(self):
        log = ["invalid log line", '127.0.0.1 - - "GET /" 200 123']
        self.assertEqual(self.analyzer.analyze(log)["total_requests"], 1)

    def test_multiple_errors(self):
        log = ['1.1.1.1 - "GET" 200', '2.2.2.2 - "GET" 500', '3.3.3.3 - "GET" 403']
        self.assertEqual(self.analyzer.analyze(log)["error_rate"], 66.67)

    def test_large_status_codes(self):
        log = ['1.1.1.1 - "GET" 503', '1.1.1.1 - "GET" 504']
        self.assertEqual(self.analyzer.analyze(log)["error_rate"], 100.0)

    def test_mixed_ips_and_status(self):
        log = ['1.1.1.1 - 200', '1.1.1.1 - 404', '2.2.2.2 - 200']
        res = self.analyzer.analyze(log)
        self.assertEqual(res["unique_visitors"], 2)
        self.assertEqual(res["total_requests"], 3)

    def test_zero_status_ignored(self):
        log = ['1.1.1.1 - 000'] # Qeyri-standart, amma xəta kimi sayılmamalı (400-dən kiçikdir)
        self.assertEqual(self.analyzer.analyze(log)["error_rate"], 0.0)

    def test_all_unique(self):
        log = ['1.1.1.1 - 200', '1.1.1.2 - 200', '1.1.1.3 - 200']
        self.assertEqual(self.analyzer.analyze(log)["unique_visitors"], 3)

if __name__ == '__main__':
    unittest.main()