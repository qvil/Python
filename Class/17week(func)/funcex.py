## header
Bible_read = open('Bible_NASB.TXT','r')

NASB_read = (Bible_read.readlines())
##

##
# find function start
##
def find():
    input_read = raw_input('What word do you want to find :')

    cnt = 0



    for line in NASB_read:
    	cnt = cnt + line.count(input_read)
    print ("find text : %s , count : %d" % (input_read,cnt))
##
# find function end
##
