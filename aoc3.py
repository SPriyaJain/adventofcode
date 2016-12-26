# Part 1
possible = 0
with open('aoc3inp.txt') as f:
	inp = f.read()
inp = inp.split("\n")
for line in inp:
	 line = line.split()
	 for i in range(3):
	 	line[i] = int(line[i])
	 line = sorted(line)
	 if line[0] + line[1] > line[2]:
	 	possible += 1
print possible

# Part 2
possible = 0
for line in range(len(inp)):
	inp[line] = inp[line].split()
for curRow in range(0, len(inp) - 2, 3):
	for n in range(3):
		curSet = []
		curSet.append(int(inp[curRow][n]))
		curSet.append(int(inp[curRow+1][n]))
		curSet.append(int(inp[curRow+2][n]))
		curSet = sorted(curSet)
		if curSet[0] + curSet[1] > curSet[2]:
			possible += 1
print possible
