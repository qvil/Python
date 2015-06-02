height = input('height(m)?:')
weight = input('weight(kg)?:')
x = weight/(height*height)
print (" %0.1f" % x)
if x<18.5:
	print 'thin'
elif 18.5<=x<23:
	print 'normal'
elif 23<=x<25:
	print 'over weight'
elif 25<=x<30:
	print 'fat 1class'
elif 30<=x<35:
	print 'fat 2class(dangerous)'
else:
	print 'fat 3class(super pig)'