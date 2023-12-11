import fileinput
import math

# initilaize map and solution grid
tiles = []
start = []
for line in fileinput.input(files='input.txt') :
	if line.find('S') != -1 :
		start = [len(tiles), line.find('S')]	
	tiles.append([x for x in line.strip()])	

pipe = []
for i in range(len(tiles)) :
	list = []
	for j in range(len(tiles[0])) :
		list.append('.')
	pipe.append(list)

pipe[start[0]][start[1]] = 'S'

# fill pipe into solution grid
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
		pipe[i2][j2] = tiles[i2][j2]
		stack.append((i2, j2))

def steps() :
	stack.append((start[0], start[1]))
	while len(stack) > 0 :
		i, j = stack.pop()
		if i > 0 and pipe[i - 1][j] == '.' :
			take_step(i, j, i - 1, j)
		if i < len(tiles) - 1 and pipe[i + 1][j] == '.':
			take_step(i, j, i + 1, j)
		if j > 0 and pipe[i][j - 1] == '.':
			take_step(i, j, i, j - 1)
		if j < len(tiles[i]) - 1 and pipe[i][j + 1] == '.':
			take_step(i, j, i, j + 1)

stack = []
steps()

# expand the grid
expanded = []
for i in range(len(pipe) * 2) :
	list = []
	for j in range(len(pipe[0]) * 2) :
		if i % 2 == 1 and j % 2 == 1 :
			list.append(pipe[int(i / 2)][int(j / 2)])
		else :
			list.append('.')
	expanded.append(list)

# connect

updates = {}
for i in range(len(expanded)) :
	for j in range(len(expanded[i])) :
		if expanded[i][j] == '|' :
			updates[(i - 1, j)] = '|'
			updates[(i + 1, j)] = '|'
		elif expanded[i][j] == '-' :
			updates[(i, j + 1)] = '-'
			updates[(i, j - 1)] = '-'
		elif expanded[i][j] == 'L' :
			updates[(i - 1, j)] = '|'
			updates[(i, j + 1)] = '-'
		elif expanded[i][j] == 'J' :
			updates[(i - 1, j)] = '|'
			updates[(i, j - 1)] = '-'
		elif expanded[i][j] == '7' :
			updates[(i + 1, j)] = '|'
			updates[(i, j - 1)] = '-'
		elif expanded[i][j] == 'F' :
			updates[(i + 1, j)] = '|'
			updates[(i, j + 1)] = '-'
for key in updates :
	i, j = key
	expanded[i][j] = updates[key]

# find outside
outside = set()
for i in range(len(expanded)) :
	outside.add((i, 0))
	outside.add((i, len(expanded[i]) - 1))
for j in range(len(expanded[0])) :
	outside.add((0, j))
	outside.add((len(expanded) - 1, j))

stack = []
for element in outside :
	stack.append(element)

while len(stack) > 0 :
	i, j = stack.pop()
	if expanded[i][j] != '.' :
		continue

	expanded[i][j] = 'O'
	if i > 0 and expanded[i - 1][j] == '.':
		stack.append((i - 1, j))
	if i < len(expanded) - 1 and expanded[i + 1][j] == '.':
		stack.append((i + 1, j))
	if j > 0 and expanded[i][j - 1] == '.':
		stack.append((i, j - 1))
	if j < len(expanded[i]) - 1 and expanded[i][j + 1] == '.':
		stack.append((i, j + 1))

count = 0
for i in range(len(expanded)) :
	for j in range(len(expanded[i])) :
		if expanded[i][j] == '.' and pipe[int(i / 2)][int(j / 2)] == '.' :
			pipe[int(i / 2)][int(j / 2)] = 'I'
			count += 1
print(count)

# for line in pipe :
# 	for val in line :
# 		print(str(val) + " ", end='')
# 	print()

