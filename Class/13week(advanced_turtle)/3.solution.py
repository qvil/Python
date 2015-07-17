import turtle
import time

forward = raw_input("forward?:")
# left = input("left?:")

f = open("info2.txt","w")
print forward
f.write(forward)
f.close()




f = open("info2.txt","r")
line = f.readlines()
# print (line[0],line[1])
f.close()

g = turtle.Turtle()
g.home
g.clear
g.forward(int(line[0]))
print("forward = %d" % (int(line[0])))
# g.left(int(line[1]))
# print("left = %d" % (int(line[1])))
# g.forward(int(line[0]))

time.sleep(5)