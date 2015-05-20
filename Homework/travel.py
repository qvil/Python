##############################################
# Date : 150520 Tue
# Author : Taesu Hyeon
# Travel Place Random Choice Program
##############################################
import random

place = [5]
cnt = 0

for i in range(0,5):
	inputval = raw_input("Input travel place : ")
	place[cnt] = inputval
	place.append(inputval)
	cnt += 1

print("travel place : %s" % (random.choice(place)))