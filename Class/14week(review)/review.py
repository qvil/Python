var = input("what number?:")
var = int(var)
for index in range(1,10):
	print ('%d x %d = %d' % (var,index,(var*index)))