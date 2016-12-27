# Part 1
import operator
with open('aoc4inp.txt') as f:
  inp = f.read()
inp = inp.split('\n')
sectorsSum = 0
realRooms = []

for line in inp:
  lineLi = []
  checkSum = ""
  sectorIDStart = 0
  realSum = ""

  for charNum in range(len(line)):
    if line[charNum] != "-":
      lineLi.append(line[charNum])
    elif line[charNum] == "-" and line[charNum+4] == "[":
      sectorIDStart = charNum + 4
      break

  for i in range(1, 6):
    checkSum += line[sectorIDStart + i]

  lineLi = sorted(lineLi)
  countDict = {}

  frequency = []
  for char in "abcdefghijklmnopqrstuvwxyz":
    countDict.update({char:lineLi.count(char)})
    frequency.append(lineLi.count(char))
  sortedCount = sorted(countDict.items(), key=operator.itemgetter(0))
  frequency = sorted(frequency)

  for n in range(5):
    for i in range(len(sortedCount)):
      if sortedCount[i][1] == frequency[25-n]:
        realSum += sortedCount[i][0]
        del sortedCount[i]
        realRooms.append(line)
        break

  if realSum == checkSum:
    sectorsSum += int(line[sectorIDStart - 3: sectorIDStart])

print sectorsSum

#Part 2
realRooms = realRooms[::5]
for line in realRooms:
  newLine = ""

  for char in range(len(line)):
    if line[char] == "[":
      sectorIDStart = char - 3
      sectorID = int(line[sectorIDStart: sectorIDStart + 3])
  sectorID = sectorID % 26

  for char in range(len(line)):
    if line[char] == '-':
      newLine += " "
    elif line[char] == '[' or line[char+3] == "[":
      break
    else:
      displacement = (sectorID + ord(line[char]) - 97) % 26
      newLine += chr(displacement + 97)

  if newLine == "northpole object storage ":
    print line[sectorIDStart: sectorIDStart + 3]
