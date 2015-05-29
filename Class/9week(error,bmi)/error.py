import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    print(a+b-c)
except:
    print('Error!')

print('End')

