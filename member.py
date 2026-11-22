class Member:
    def __init__(self, name, visits, months, monthly_fee):
        self.name = name
        self.visits = visits
        self.months = months
        self.monthly_free = monthly_fee

    def is_at_risk(self, min_visits=4, min_months=6):
        return self.visits < min_visits and self.months > min_months

    def total_paid(self):
        return self.months * self.monthly_free

    def summary(self):
        return f"ชื่อสมาชิก : {self.name} | เสี่ยงเลิกใช้บริการ : {self.is_at_risk()} | ที่ค่าบริการ: {self.total_paid()} บาท"


m1 = Member("phongkrit boulowpetch", 2, 10, 900)
m2 = Member("อนิทุน โชคช่วย", 2, 5, 900)
m3 = Member("ทวิน โชคช่วย", 2, 2, 900)
m4 = Member("ปกรณื โชคช่วย", 2, 2, 900)

members = [m1, m2, m3, m4]

# 1. เรียกใช้ด้วยเกณฑ์เริ่มต้น (ไม่ส่งค่าเข้าไป -> ใช้ 4 และ 6)
print("--- เกณฑ์เริ่มต้น (visits < 4 และ months > 6) ---")
for m in members:
    if m.is_at_risk():
        print(m.summary())

# 2. ทดลองเรียกใช้ด้วยเกณฑ์อื่น (เช่น visits < 4 และ months > 3)
print("\n--- เกณฑ์ใหม่ (visits < 4 และ months > 3) ---")
for m in members:
    if m.is_at_risk(4, 3):
        print(f"ชื่อสมาชิก : {m.name} | เสี่ยง (เกณฑ์ใหม่) : True")