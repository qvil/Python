r_file = open('read.txt','r')
for line in r_file:
	print (line.strip())
r_file.close()