# r_file = open('read.txt','r')
# print_file = r_file.readlines()
# print (print_file[0:])




r_file = open('read.txt','r')
for line in r_file:
	print (line.strip())