# 1, 2 주석처리 하여 차이점 알아보기
# marks = [90,85,80,75,50]

# number = 0
# for mark in marks:
# 	number = number + 1
# 	if mark >= 60:
# 		# print("%d번 학생은 합격." , number); # 1
# 		print("%d번 학생은 합격." % number); # 2
# 	else:
# 		# print("%d번 학생은 불합격.",  number); # 1
# 		print("%d번 학생은 불합격."%  number); # 2

#################################################################

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
	number = number +1
	if mark < 60: continue
		print("%d번 학생은 합격." % number)


# marks = [90, 25, 67, 45, 80]

# number = 0
# for mark in marks:
#     number = number +1
#     if mark < 60: continue
#     print("%d번 학생 축하합니다. 합격입니다. " % number)
