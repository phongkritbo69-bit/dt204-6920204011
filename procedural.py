name = "phongkrit boulowpetch"
visits = 10
months = 10

#ฟังชันก์สำหรับตรวจสอบความเสี่ยง
def is_at_risk(visits, months):
    return visits < 4 and months > 6

print("ชื่อสมาชิก :", name)
print("จำนวนครั้งที่ใช้งาน", visits, "ครั้ง")
print("อายุสมาชิก", months ,"เดือน")
print("เสี่ยงเลิกใช้บริการ :", is_at_risk(visits, months))

#test1