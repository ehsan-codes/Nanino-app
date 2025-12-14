class NaninoAnalyzer:
    def __init__(self, worked_days: int, off_days: int, total_bakes: int,
                 total_bags: int, month_days: int):
        self.worked_days = worked_days
        self.off_days = off_days
        self.total_bakes = total_bakes
        self.total_bags = total_bags
        self.month_days = month_days

    def calculate(self) -> dict:
        total_quota = self.total_bags * 113
        daily_quota = total_quota / self.month_days
        expected_bakes = daily_quota * self.worked_days
        diff = self.total_bakes - expected_bakes

        if diff < 0:
            status = f"کم‌پختی: {abs(int(diff))} نان کمتر از سهمیه"
        elif diff > 0:
            status = f"زیادپختی: {int(diff)} نان بیشتر از سهمیه"
        else:
            status = "دقیقاً مطابق سهمیه پختی"

        return {
            "total_quota": total_quota,
            "daily_quota": int(daily_quota),
            "expected_bakes": int(expected_bakes),
            "total_bakes": self.total_bakes,
            "off_days": self.off_days,
            "status": status
        }