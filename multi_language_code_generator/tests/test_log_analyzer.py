import unittest
from reference.log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_empty_log(self):
        # 1. Boş log siyahısı
        res = self.analyzer.analyze([])
        self.assertEqual(res["total_requests"], 0)
        self.assertEqual(res["error_rate"], 0)

    def test_single_success(self):
        # 2. Tək bir uğurlu sorğu
        log = ['127.0.0.1 - - [10/May/2026] "GET /" 200 123']
        res = self.analyzer.analyze(log)
        self.assertEqual(res["total_requests"], 1)
        self.assertEqual(res["error_rate"], 0.0)

    def test_single_error(self):
        # 3. Tək bir xəta sorğusu (404)
        log = ['192.168.1.1 - - [10/May/2026] "POST /login" 404 500']
        res = self.analyzer.analyze(log)
        self.assertEqual(res["error_rate"], 100.0)

    def test_unique_visitors(self):
        # 4. Eyni IP-dən gələn fərqli sorğular (Unikal ziyarətçi 1 olmalıdır)
        log = [
            '1.1.1.1 - - [10/May] "GET /" 200 100',
            '1.1.1.1 - - [10/May] "GET /about" 200 150'
        ]
        res = self.analyzer.analyze(log)
        self.assertEqual(res["unique_visitors"], 1)

    def test_multiple_visitors(self):
        # 5. Fərqli IP-lər
        log = [
            '1.1.1.1 - - [10/May] "GET /" 200 100',
            '2.2.2.2 - - [10/May] "GET /" 200 100'
        ]
        res = self.analyzer.analyze(log)
        self.assertEqual(res["unique_visitors"], 2)

    def test_malformed_lines(self):
        # 6. Səhv formatlı sətirlər (nəzərə alınmamalıdır)
        log = ["invalid log line", "short line 200"]
        res = self.analyzer.analyze(log)
        self.assertEqual(res["total_requests"], 0)

    def test_mixed_results(self):
        # 7. Qarışıq uğurlu və xətalı sorğular
        log = [
            '1.1.1.1 - - [10/May] "GET /" 200 100',
            '1.1.1.1 - - [10/May] "GET /" 500 100'
        ]
        res = self.analyzer.analyze(log)
        self.assertEqual(res["error_rate"], 50.0)

    def test_server_error_5xx(self):
        # 8. Server xətası (503)
        log = ['1.1.1.1 - - [10/May] "GET /" 503 0']
        res = self.analyzer.analyze(log)
        self.assertEqual(res["error_rate"], 100.0)

    def test_large_status_codes(self):
        # 9. Qeyri-adi amma keçərli status kodları
        log = ['1.1.1.1 - - [10/May] "GET /" 499 0']
        res = self.analyzer.analyze(log)
        self.assertEqual(res["error_rate"], 100.0)

    def test_zero_requests_calculation(self):
        # 10. Sıfır sorğu zamanı division by zero xətası olmamalıdır
        res = self.analyzer.analyze(["   "])
        self.assertEqual(res["error_rate"], 0)

if __name__ == '__main__':
    unittest.main()