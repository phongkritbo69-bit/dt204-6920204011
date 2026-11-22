class Member:
    def __init__(self, name, visits):
        self.name = name
        self.visits = visits

    def is_at_risk(self):
        return self.visits < 4

m1 = Member('สมชาย', 2)
m2 = Member('สมหญิง', 12)
print(m1.is_at_risk(), m2.is_at_risk())
