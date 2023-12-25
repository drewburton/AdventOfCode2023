class Beam :
	def __init__(self, row, column, direction) :
		self.row = row
		self.column = column
		self.direction = direction

def next(beam) :
	row, column, direction = beam
	next_row = row
	next_column = column
	if direction == 'r' :
		next_column += 1
	elif direction == 'l' :
		next_column -= 1
	elif direction == 'u' :
		next_row -= 1
	else :
		next_row += 1
	
	if next_row < 0 or next_column < 0 or next_row >= len(grid) or next_column >= len(grid[0]) :
		return None

	# empty space
	if grid[next_row][next_column] == '.' :
		return [(next_row, next_column, direction)]
	# passing through pointy end of horizontal splitter
	if (direction == 'r' or direction == 'l') and grid[next_row][next_column] == '-' :
		return [(next_row, next_column, direction)]
	# passing through pointy end of vertical splitter
	if (direction == 'u' or direction == 'd') and grid[next_row][next_column] == '|' :
		return [(next_row, next_column, direction)]
	if grid[next_row][next_column] == '/' :
		if direction == 'r' :
			return [(next_row, next_column, 'u')]
		if direction == 'l' :
			return [(next_row, next_column, 'd')]
		if direction == 'u' :
			return [(next_row, next_column, 'r')]
		if direction == 'd' :
			return [(next_row, next_column, 'l')]
	if grid[next_row][next_column] == '\\' :
		if direction == 'r' :
			return [(next_row, next_column, 'd')]
		if direction == 'l' :
			return [(next_row, next_column, 'u')]
		if direction == 'u' :
			return [(next_row, next_column, 'l')]
		if direction == 'd' :
			return [(next_row, next_column, 'r')]
	if grid[next_row][next_column] == '-' :
		return [(next_row, next_column, 'l'), (next_row, next_column, 'r')]
	if grid[next_row][next_column] == '|' :
		return [(next_row, next_column, 'u'), (next_row, next_column, 'd')]

grid = []
for l in open('input.txt') :
	grid.append(list(l.strip()))

beams = []
beams.append((0, -1, 'r'))
energized = set()
while len(beams) > 0 :
	next_beams = []
	for beam in beams :
		new = next(beam)
		if new is not None :
			for x in new :
				if x not in energized :
					energized.add(x)
					next_beams.append(x)

	beams = next_beams

cells = set()
for beam in energized :
	r, c, d = beam
	cells.add((r, c))

print(len(cells))

# for i in range(len(grid)) :
# 	for j in range(len(grid[i])) :
# 		if (i, j) in cells :
# 			print('#', end='')
# 		else :
# 			print('.', end='')
# 	print()