# 类的声明
class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker('bob smith', 10000)
james = Worker('lebron james', 2000000)

print(bob.lastName())
james.giveRaise(1)
print(james.pay)
print(james.name)

#第四章结束,本章主要介绍了一些核心数据类型.但没有很多细节.