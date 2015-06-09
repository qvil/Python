#!/usr/bin/python #
# -*- coding: utf-8 -*- #

# ########## first step
# f = open("newfile.txt", 'a')
#
# for index in range(11,20):
#     data = "%d line.\n" % index
#     f.write(data)
# f.close()
# ##########

########## tell(), seek()
f = open("newfile.txt", 'r')
f.readline()
print(f.tell())
f.seek(0)
print(f.tell())

##########
