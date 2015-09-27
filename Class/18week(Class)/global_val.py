glo = 1

def adder():
    global glo
    local = 2
    glo = glo + 10
    local = local + 10
    print("glo : %d" % (glo))
    print("local : %d" % (local))

adder()
adder()
adder()
print(glo)
# print(local)
