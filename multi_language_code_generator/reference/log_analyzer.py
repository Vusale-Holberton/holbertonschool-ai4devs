class LogAnalyzer:
    def parse_line(self, line: str) -> dict:
        """
        Log sətrini parçalayır və status kodu ilə IP ünvanını çıxarır.
        """
        parts = line.split()
        # Standart log formatında IP 0-cı, Status isə 8-ci indeksdə olur
        if len(parts) < 9:
            return None
        
        try:
            return {
                "ip": parts[0],
                "status": int(parts[8])
            }
        except (ValueError, IndexError):
            return None

    def analyze(self, lines: list) -> dict:
        """
        Log sətirlərinin siyahısını analiz edir və statistik nəticə qaytarır.
        """
        total = 0
        errors = 0
        unique_ips = set()

        for line in lines:
            data = self.parse_line(line)
            if data:
                total += 1
                unique_ips.add(data["ip"])
                # 400 və daha yuxarı status kodları xəta hesab olunur
                if data["status"] >= 400:
                    errors += 1
        
        # Xəta dərəcəsini hesabla (faizlə)
        error_rate = (errors / total * 100) if total > 0 else 0
        
        return {
            "total_requests": total,
            "unique_visitors": len(unique_ips),
            "error_rate": round(error_rate, 2)
        }