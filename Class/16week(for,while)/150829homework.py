input_read_file = open('read.txt','r')
input_read = raw_input('What fruit do you want to find :')
cnt = 0



for line in input_read_file:
	cnt = cnt + line.count(input_read)
print ("find text : %s , count : %d" % (input_read,cnt))
input_read_file.close()
