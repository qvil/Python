Bible_read = open('Bible_NASB.TXT','r')

NASB_read = (Bible_read.readlines())

input_read = raw_input('What word do you want to find :')

cnt = 0



for line in NASB_read:
	cnt = cnt + line.count(input_read)
print ("find text : %s , count : %d" % (input_read,cnt))

# for index in range(0,len(NASB_read)):
	# print NASB_read[index]
print NASB_read[10]
print line.index("Jesus")

# print NASB_read.index("God")


Bible_read.close()
