test_read = open('project.txt','r')

all_read  = (test_read.readlines())

# print all_read[0]
# print all_read[1]
# print all_read[2]
# print all_read[3]

def find():
	input_read = raw_input('test :')

	cnt = 0
#
	for line in all_read:
		cnt = cnt + line.count(input_read)
        ts = 1

        if "ssun" == input_read:
            print ("line : %d" % (ts))
        else:
            ts = ts+1

        print ("find text : %s , count : %d" % (input_read,cnt))
        #
        # for index in range(0,len(all_read)):
        #     print all_read[index]
        #     print index+1



find()
##

# for index in range(0,len(all_read)):
#     print all_read[index]
#     print index+1
