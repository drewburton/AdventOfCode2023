
def cycle(grid) :
	for i in range(4) :
		grid = tilt(grid)
		grid = rotatecw(grid)
	return grid

def rotatecw(grid) :
	new = ''
	g = grid.split('\n')
	for j in range(len(g[0])) :
		line = ''
		for i in range(len(g) - 1, -1, -1) :
			line += g[i][j]
		new += line + '\n'
	return new[:-1]

def tilt(grid) :
	g = grid.split('\n')
	for r in range(len(g)) :
		open = -1
		for c in range(len(g[r])) :
			if open == -1 and g[r][c] == '.' :
				open = c
			if g[r][c] == '#' :
				open = -1
			if open != -1 and g[r][c] == 'O' :
				s = list(g[r])
				s[c] = '.'
				s[open] = 'O'
				g[r] = ''.join(s)
				open += 1
	return '\n'.join(g)

def load(grid) :
	load = 0
	g = grid.split('\n')
	for r in range(len(g)) :
		for c in range(len(g[r])) :
			if g[r][c] == 'O' :
				load += len(g) - r
	return load

grid = ''
for l in open('input.txt') :
	grid += l

for i in range(3) :
	grid = rotatecw(grid)

state = {}
i = 0
while not state.get(grid) :
	state[grid] = i
	grid = cycle(grid)
	if state.get(grid) :
		remaining = (1000000000 - (i + 1)) % ((i + 1) - state.get(grid))
		for i in range(remaining) :
			grid = cycle(grid)
		break
	i += 1
grid = rotatecw(grid)
print(load(grid))