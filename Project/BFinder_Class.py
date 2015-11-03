# -*- coding:utf-8 -*-
Bible_read = open('Bible_NASB.TXT','r')
NASB_read = (Bible_read.readlines())

class BFinder:
    # def __init__(self):
    def start(self):
        self.ui()

    def ui(self):
        print("\n#########################")
    	print("#   Bible Fineder v1.0  #")
    	print("#     1. Find Word      #")
    	print("#     2. Exit           #")
    	print("#########################")

    	mode = input("select mode : ")

    	if mode == 1:
    		self.find()
    	elif mode == 2:
    		print("\nThanks for using \nMade By Ssun and Taesu")
    		exit()
        else:
            print("Wrong Input. Try Again")
            self.start()

    def find(self):
    	input_read = raw_input('What word do you want to find :')
    	cnt = 0
        string = "testtesttest\n"
        # print(NASB_read[2:4])
        # print("linelineline : %s" %(string.find("\n")))
    	for line in NASB_read:
    		cnt = cnt + line.count(input_read)
    	print ("find text : %s , count : %d" % (input_read, cnt))

bfinder = BFinder()
bfinder.start()
Bible_read.close()
