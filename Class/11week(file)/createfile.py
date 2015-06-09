#!/usr/bin/python #
# -*- coding: utf-8 -*- #
f = open("newfile.txt", 'w')

for i in range(1,11):
    data = "%d line\n" % i  # \n 는 개행문자 -> 엔터키(줄바꿈)
    f.write(data)
f.close()
