import unittest
from reference.log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_status_200(self):
        line = '127.0.0.1 - - [10/May/2026] "GET /" 200 1024'
        self.assertEqual(self.analyzer.parse_line(line)["status"], 200)

    def test_status_404(self):
        line = '127.0.0.1 - - [10/May/2026] "GET /none" 404 512'
        self.assertEqual(self.analyzer.parse_line(line)["status"], 404)

    def test_status_500(self):
        line = '127.0.0.1 - - [10/May/2026] "POST /api" 500 256'
        self.assertEqual(self.analyzer.parse_line(line)["status"], 500)

    def test_empty_list(self):
        self.assertEqual(self.analyzer.analyze([])["total_requests"], 0)

    def test_error_rate_50_percent(self):
        logs = ['... "GET /" 200 ...', '... "GET /" 404 ...']
        self.assertEqual(self.analyzer.analyze(logs)["error_rate"], 50.0)

    def test_malformed_line(self):
        self.assertEqual(self.analyzer.parse_line("bad data")["status"], 0)

    def test_status_301(self):
        line = '... "GET /" 301 ...'
        self.assertEqual(self.analyzer.parse_line(line)["status"], 301)

    def test_status_403(self):
        line = '... "GET /" 403 ...'
        self.assertEqual(self.analyzer.parse_line(line)["status"], 403)

    def test_all_errors(self):
        logs = ['... "GET /" 500 ...', '... "GET /" 400 ...']
        self.assertEqual(self.analyzer.analyze(logs)["error_rate"], 100.0)

    def test_all_success(self):
        logs = ['... "GET /" 200 ...', '... "GET /" 200 ...']
        self.assertEqual(self.analyzer.analyze(logs)["error_rate"], 0.0)

if __name__ == '__main__':
    unittest.main()