# Date : 150504
# Author : tshyeon
# file name : calculator.py

########### Function ############
def add(a,...):
	return a+b

def sub(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	print("share : %d" % (a/b))
	print("rest : %d" % (a%b))
########### Function ############

########### Interface ############
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. exit")
########### Interface ############

########### Menu Process ############
mode = int(input('mode : '))

if(mode == 1):
	num1 = int(input('num1 : '))
	num2 = int(input('num2 : '))
	print(add(num1,num2))
	# print(mode)
elif(mode == 2):
	print(mode)
elif(mode == 3):
	print(mode)
elif(mode == 4):
	num1 = int(input('num1 : '))
	num2 = int(input('num2 : '))
	div(num1,num2)
elif(mode == 5):
	exit()
else:
	print('Please input 1~5 number')
########### Menu Process ############