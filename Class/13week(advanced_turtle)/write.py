def write():
	forward = raw_input("forward? = ")
	left = raw_input("left? =")



	w = open("write.txt","w")
	w.write(forward + "\n")

	w.write(left)
	w.close()

