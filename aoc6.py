import operator
import collections
with open('aoc6inp.txt') as f:
  inp = f.read()
inp = inp.split('\n')
message = ""

# Part 1
for column in range(8):
    letters = []
    for i in range(len(inp)):
        letters.append(inp[i][column])
    message += collections.Counter(letters).most_common(1)[0][0]
print "Part 1 answer: " + message

# Part 2
message = ""
for column in range(8):
    letters = []
    for i in range(len(inp)):
        letters.append(inp[i][column])
    message += collections.Counter(letters).most_common()[len(collections.Counter(letters).most_common()) - 1][0]
print "Part 2 answer: " + message
