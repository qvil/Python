# Date : 2015.05.27.Tue
# Author : Taesu Hyeon
# File name : bmi.py
#-*- coding: euc-kr -*-

# Level 1
# height_cm = input('Input height(cm) : ')
# weight = input('Input weight(kg) : ')
# height_m = height_cm / 100.0
# bmi = (weight) / (height_m * height_m)
# print('bmi : %f' % (bmi))

# Level 2
height_cm = input('Input height(cm) : ')
weight = input('Input weight(kg) : ')
height_m = height_cm / 100.0
bmi = (weight) / (height_m * height_m)

if bmi < 18.5:
    print('bmi : %f, thin' % (bmi))
elif (bmi >= 18.5 and bmi < 25):
    print('bmi : %f, normal' % (bmi))
elif (bmi >= 25 and bmi < 30):
    print('bmi : %f, fat' % (bmi))
else:
    print('bmi : %f, very fat' % (bmi))
