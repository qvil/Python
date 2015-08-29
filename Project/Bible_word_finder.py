Bible_read = open('Bible_NASB.TXT','r')
input_read = raw_input('What word do you want to find :')
cnt = 0



for line in Bible_read:
	cnt = cnt + line.count(input_read)
print ("find text : %s , count : %d" % (input_read,cnt))
Bible_read.close()