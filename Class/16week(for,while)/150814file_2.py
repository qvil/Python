r_file = open('read.txt','r')


cnt = 0

for line in r_file:
	# print (line.strip())
	# print (line.count('soon'))    
	cnt = cnt + line.count('soon')

print ("cnt : %d" % cnt)	



r_file.close()

print ("find text : %s , count : %d" % cnt)	