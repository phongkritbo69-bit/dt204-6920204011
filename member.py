class Member:
    def __init__(self, name, visits, months, monthly_fee):
        self.name = name 
        self.visits = visits
        self.months = months
        self.monthly_free = monthly_fee
        

    def is_at_risk(self):
        return self.visits < 4 and self.months > 6 
    def total_paid(self):
            return self.months * self.monthly_free
        

m1 = Member("phongkrit boulowpetch", 2, 10, 900)
print("ชื่อสมาชิก :", m1.name)
print("เสี่ยงเลิกใช้บริการ", m1.is_at_risk())
print("ที่ค่าบริการ: ", m1.total_paid(), "บาท")

m2 = Member("อนิทุน โชคช่วย", 2, 5, 900)
print("ชื่อสมาชิก :", m2.name)
print("เสี่ยงเลิกใช้บริการ", m2.is_at_risk())
print("ที่ค่าบริการ: ", m2.total_paid(), "บาท")

m3 = Member("ทวิน โชคช่วย", 2, 2, 900)
print("ชื่อสมาชิก :", m3.name)
print("เสี่ยงเลิกใช้บริการ", m3.is_at_risk())
print("ที่ค่าบริการ: ", m3.total_paid(), "บาท")