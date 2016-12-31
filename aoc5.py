import hashlib
door = "cxdnnyjw"

# Part 1
code = ""
i = 0
while len(code) < 8:
    mhash = hashlib.md5(door + str(i)).hexdigest()
    if mhash[:5] == "00000":
        code += str(mhash[5])
    i += 1
print "Part 1 answer: " + code

# Part 2
code = "........"
i = 0
while "." in code:
    mhash = hashlib.md5(door + str(i)).hexdigest()
    if mhash[:5] == "00000" and unicode(mhash[5]).isnumeric() and int(mhash[5]) < 8:
        if code[int(mhash[5])] == ".":
            code = code[:int(mhash[5])] + mhash[6] + code[int(mhash[5]) + 1:]
    i += 1
print code
