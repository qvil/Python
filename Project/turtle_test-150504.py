import turtle
import random
geobuk = turtle.Turtle()


geobuk.shape('turtle')
geobuk.shapesize(2,2,3)

# geobuk.circle(150)

###################### circle
geobuk.home()
geobuk.clear()
geobuk.penup()
geobuk.forward(200)
geobuk.left(90)
geobuk.pendown()
geobuk.circle(200)
geobuk.penup()
geobuk.home()
geobuk.pendown()
###################
while True:
	geobuk.left(random.randint(1,360))
	geobuk.forward(30)
	
	if geobuk.distance(0,0) > 200:
		geobuk.undo()



# cnt = 0
# while cnt != 3:
# 	geobuk.forward(200)
# 	geobuk.left(120)
# 	geobuk.forward(200)
# 	geobuk.left(120)
# 	geobuk.forward(200)
# 	cnt+=1