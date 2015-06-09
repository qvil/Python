#!/usr/bin/python #
# -*- coding: utf-8 -*- #

########## first step
# f = open("newfilew.txt", 'r')
# line = f.readline()
# print(line)
# f.close()
##########

# ########## second step
# f = open("newfile.txt", 'r')
# lines = f.readlines()
#
# # print(lines)
# for line in lines:
#     print(line)
# 
# f.close()
# ##########

########## third step
f = open("newfile.txt", 'r')
data = f.read()

print(data)

f.close()
##########
