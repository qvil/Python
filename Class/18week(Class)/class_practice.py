class Calculator:
	def __init__(self):
		self.result = 0

	def plus(self,num):
		self.result += num
		return self.result

	def minus(self,num):
		self.result -= num
		return self.result

	def times(self,num):
		self.result *= num
		return self.result

	def divided_by(self,num):
		self.result /= num
		return self.result

cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()
cal4 = Calculator()

print (cal1.plus(2))
print (cal1.times(115))
print (cal1.divided_by(13))
print (cal1.minus(44))