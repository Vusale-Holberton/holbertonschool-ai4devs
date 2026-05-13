class LogAnalyzer:
    def parse_line(self, line: str) -> dict:
        try:
            parts = line.split()
            status_code = int(parts[8])
            return {"status": status_code}
        except (IndexError, ValueError):
            return {"status": 0}

    def analyze(self, lines: list) -> dict:
        total = len(lines)
        if total == 0:
            return {"total_requests": 0, "error_rate": 0.0}

        errors = sum(1 for l in lines if self.parse_line(l)["status"] >= 400)
        error_rate = (errors / total) * 100
        
        return {
            "total_requests": total, 
            "error_rate": round(error_rate, 2)
        }