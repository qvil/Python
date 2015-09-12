# r_file = open('read.txt','r')
# print_file = r_file.readlines()
# print (print_file[0:])




r_file = open('read.txt','r')

read_r = (r_file.readlines())

for index in range(0,len(read_r)):
	print read_r[index]

print read_r[10]




# for line in read_r
# 	print line
# for line in r_file:
	# line
# print read_r[1]
# print read_r[2]
# print read_r[3]
