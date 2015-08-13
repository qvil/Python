tall = input("tall? = ")
weight = input("weight? = ") 
tall_m = tall/100.0
x = (weight/(tall_m*tall_m))
print x

if x < 18.5:
    print('x : %f, thin' % (x))
elif (x >= 18.5 and x < 25):
    print('x : %f, normal' % (x))
elif (x >= 25 and x < 30):
    print('x : %f, fat' % (x))
else:
    print('x : %f, very fat' % (x))
