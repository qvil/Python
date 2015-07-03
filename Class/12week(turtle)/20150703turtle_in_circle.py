import turtle
import random

g = turtle.Turtle()

g.home()
g.clear()
g.forward(200)
g.left(90)
g.circle(200)
g.home()

while g.distance(0,0) < 200:
	print(g.distance(0,0))
	g.left(random.randint(1,360))
	g.forward(100)

# while cnt < 100:
	# forward()
	