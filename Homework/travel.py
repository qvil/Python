a = [5]
cnt = 0
for i in range(0,4):
	inputval = input("Input travel place : ")
	a[cnt] = inputval
	a.append(inputval)
	cnt += 1
print(a)