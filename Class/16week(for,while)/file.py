read_file = open('read.txt','w')
name_input = raw_input("What your name?")
read_file.write("Hello\n")
read_file.write(name_input)