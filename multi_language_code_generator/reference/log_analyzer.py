class LogAnalyzer:
    def parse_line(self, line: str) -> dict:
        parts = line.split()
        if len(parts) < 9:
            return None
        return {"ip": parts[0], "status": int(parts[8])}

    def analyze(self, lines: list) -> dict:
        total, errors, unique_ips = 0, 0, set()
        for line in lines:
            data = self.parse_line(line)
            if data:
                total += 1
                unique_ips.add(data["ip"])
                if data["status"] >= 400:
                    errors += 1
        error_rate = (errors / total * 100) if total > 0 else 0
        return {"total_requests": total, "unique_visitors": len(unique_ips), "error_rate": round(error_rate, 2)}