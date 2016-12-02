li = "L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5"
answerx = 0
answery = 0
li = li.split(", ")
direction = "N"

for i in li:
	scalar = i[1:]
	
	scalar = int(scalar)
	movement = i[0]
	if movement == "L":
		if direction == "N":
			direction = "W"
			answerx -= scalar
		elif direction == "S":
			direction = "E"
			answerx += scalar
		elif direction == "E":
			direction = "N"
			answery += scalar
		else:
			direction = "S"
			answery -= scalar
	else:
		if direction == "S":
			direction = "W"
			answerx -= scalar
		elif direction == "N":
			direction = "E"
			answerx += scalar
		elif direction == "W":
			direction = "N"
			answery += scalar
		else:
			direction = "S"
			answery -= scalar
answer = abs(answerx) + abs(answery)
print answer