# -*- coding:utf-8 -*-
# 한글 사용 위해
result = 0
result1 = 0;
result2 = 0;

def adder1(num):
    global result1 # global 선언해야 global변수 사용가능
    result1 += num
    return result1

def adder2(num):
    global result2 # global 선언해야 global변수 사용가능
    result2 += num
    return result2

print(adder1(3))
print(adder1(7))
print(adder2(1))
print(adder2(6))


# class Test:
#     def prt():
#         print("hi")
# test = Test()
# test.prt()

########################################
class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self,num):
        self.result += num
        return self.result
    

cal1 = Calculator() # 생성자를 이용해서 Calculator클래스를 cal1변수에 담음
cal2 = Calculator() # 생성자를 이용해서 Calculator클래스를 cal2변수에 담음

print(cal1.adder(3))
print(cal1.adder(7))
print(cal2.adder(1))
print(cal2.adder(6))

class Test:
    test = "test"

    def tprint(self):
        print("tprint")

def fprint():
    print("fprint")

# a = Test()
# print(a.test)
# a.tprint()
# fprint()
