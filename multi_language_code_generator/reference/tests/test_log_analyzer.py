import unittest
from reference.log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_1(self): self.assertEqual(self.analyzer.analyze([])["total_requests"], 0)
    def test_2(self): self.assertEqual(self.analyzer.analyze(['1.1.1.1 - 200'])["total_requests"], 1)
    def test_3(self): self.assertEqual(self.analyzer.analyze(['1.1.1.1 - 404'])["error_rate"], 100.0)
    def test_4(self): self.assertEqual(self.analyzer.analyze(['1.1.1.1 - 200', '1.1.1.1 - 200'])["unique_visitors"], 1)
    def test_5(self): self.assertEqual(self.analyzer.analyze(['1.1.1.1 - 200', '2.2.2.2 - 200'])["unique_visitors"], 2)
    def test_6(self): self.assertEqual(self.analyzer.analyze(["invalid line"])["total_requests"], 0)
    def test_7(self): self.assertEqual(self.analyzer.analyze(['1.1.1.1 - 500'])["error_rate"], 100.0)
    def test_8(self): self.assertEqual(self.analyzer.analyze(['1.1.1.1 - 200', '1.1.1.1 - 400'])["error_rate"], 50.0)
    def test_9(self): self.assertEqual(self.analyzer.analyze(['1.1.1.1 - 301'])["error_rate"], 0.0)
    def test_10(self): self.assertEqual(self.analyzer.analyze(['1.1.1.1 - 200', '1.1.1.2 - 404', '1.1.1.3 - 500'])["total_requests"], 3)

if __name__ == '__main__':
    unittest.main()