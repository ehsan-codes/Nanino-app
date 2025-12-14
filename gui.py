import tkinter as tk
from tkinter import messagebox
from analyzer import NaninoAnalyzer

class NaninoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("نانینو - تحلیل سهمیه پخت نان")
        self.root.geometry("900x600")
        self.font_style = ("Tahoma", 14)

        self._build_widgets()

    def _build_widgets(self):
        tk.Label(self.root, text="تعداد روزهای کاری (پخت شده):",
                 font=self.font_style).grid(row=0, column=0, pady=5)
        self.entry_worked_days = tk.Entry(self.root, font=self.font_style, width=20)
        self.entry_worked_days.grid(row=0, column=1, pady=5)

        tk.Label(self.root, text="تعداد روزهای تعطیل:",
                 font=self.font_style).grid(row=1, column=0, pady=5)
        self.entry_off_days = tk.Entry(self.root, font=self.font_style, width=20)
        self.entry_off_days.grid(row=1, column=1, pady=5)

        tk.Label(self.root, text="تعداد نان پخته شده تا امروز:",
                 font=self.font_style).grid(row=2, column=0, pady=5)
        self.entry_bakes = tk.Entry(self.root, font=self.font_style, width=20)
        self.entry_bakes.grid(row=2, column=1, pady=5)

        tk.Label(self.root, text="سهمیه کیسه آرد (مثلاً ۱۸۰):",
                 font=self.font_style).grid(row=3, column=0, pady=5)
        self.entry_bags = tk.Entry(self.root, font=self.font_style, width=20)
        self.entry_bags.grid(row=3, column=1, pady=5)

        tk.Label(self.root, text="تعداد روزهای ماه (۳۰ یا ۳۱):",
                 font=self.font_style).grid(row=4, column=0, pady=5)
        self.entry_month_days = tk.Entry(self.root, font=self.font_style, width=20)
        self.entry_month_days.grid(row=4, column=1, pady=5)

        tk.Button(self.root, text="تحلیل کن", command=self.analyze,
                  font=self.font_style).grid(row=5, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(self.root, text="", justify="left",
                                     fg="blue", font=("Tahoma", 14))
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def analyze(self):
        try:
            analyzer = NaninoAnalyzer(
                worked_days=int(self.entry_worked_days.get()),
                off_days=int(self.entry_off_days.get()),
                total_bakes=int(self.entry_bakes.get()),
                total_bags=int(self.entry_bags.get()),
                month_days=int(self.entry_month_days.get())
            )
            result = analyzer.calculate()
            self.result_label.config(text=f"""
🔢 سهمیه کل: {result['total_quota']}
📆 سهمیه روزانه: {result['daily_quota']}
📊 باید تا امروز (با {analyzer.worked_days} روز کاری) می‌پختی: {result['expected_bakes']}
✅ تو پختی: {result['total_bakes']}
🛑 روزهای تعطیل: {result['off_days']}
📌 نتیجه: {result['status']}
""")
        except ValueError:
            messagebox.showerror("خطا", "لطفاً همه‌ی فیلدها را درست پر کن!")