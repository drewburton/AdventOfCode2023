import fileinput
import math

tiles = []
start = []
for line in fileinput.input(files='input.txt') :
	if line.find('S') != -1 :
		start = [len(tiles), line.find('S')]	
	tiles.append([x for x in line.strip()])	

solution = []
for i in range(len(tiles)) :
	list = []
	for j in range(len(tiles[0])) :
		list.append(float('inf'))
	solution.append(list)

solution[start[0]][start[1]] = 0

def connects(i1, j1, i2, j2) :
	# if statement checks whether current pipe location connects to adjacent
	# return statement checks whether adjacent pipe connects to current
	if i2 > i1 and (tiles[i1][j1] == 'S' or tiles[i1][j1] == '|' or tiles[i1][j1] == '7' or tiles[i1][j1] == 'F'):
		return tiles[i2][j2] == '|' or tiles[i2][j2] == 'L' or tiles[i2][j2] == 'J'
	if i2 < i1 and (tiles[i1][j1] == 'S' or tiles[i1][j1] == '|' or tiles[i1][j1] == 'L' or tiles[i1][j1] == 'J'):
		return tiles[i2][j2] == '|' or tiles[i2][j2] == '7' or tiles[i2][j2] == 'F'
	if j2 > j1 and (tiles[i1][j1] == 'S' or tiles[i1][j1] == '-' or tiles[i1][j1] == 'L' or tiles[i1][j1] == 'F'):
		return tiles[i2][j2] == '-' or tiles[i2][j2] == 'J' or tiles[i2][j2] == '7'
	if j2 < j1 and (tiles[i1][j1] == 'S' or tiles[i1][j1] == '-' or tiles[i1][j1] == 'J' or tiles[i1][j1] == '7'):
		return tiles[i2][j2] == '-' or tiles[i2][j2] == 'L' or tiles[i2][j2] == 'F'
	return False

def take_step(i1, j1, i2, j2) :
	if connects(i1, j1, i2, j2) :
		solution[i2][j2] = min(solution[i2][j2], solution[i1][j1] + 1)
		stack.append((i2, j2, i1, j1))

def steps() :
	stack.append((start[0], start[1], start[0], start[1]))
	while len(stack) > 0 :
		i, j, si, sj = stack.pop()
		if i > 0 and si != i - 1:
			take_step(i, j, i - 1, j)
		if i < len(tiles) - 1 and si != i + 1:
			take_step(i, j, i + 1, j)
		if j > 0 and sj != j - 1:
			take_step(i, j, i, j - 1)
		if j < len(tiles[i]) - 1 and sj != j + 1:
			take_step(i, j, i, j + 1)

stack = []
steps()

max = 0
for line in solution :
	for val in line :
		#print(str(val) + " ", end='')
		if not math.isinf(val) :
			max = val if val > max else max
	#print()
print(max)