def summarize(grid) :
	for i in range(len(grid) - 1) :
		if is_horizontal_reflection(i, i + 1, False) :
			return 100 * (i + 1)
	for i in range(len(grid[0]) - 1) :
		if is_vertical_reflection(i, i + 1, False) :
			return i + 1
	return -1

def is_horizontal_reflection(r1, r2, flipped) :
	if r1 < 0 or r2 >= len(grid) :
		return flipped
	
	for c in range(len(grid[r1])) :
		if grid[r1][c] != grid[r2][c] and flipped:
			return False
		elif grid[r1][c] != grid[r2][c] :
			flipped = True

	return is_horizontal_reflection(r1 - 1, r2 + 1, flipped)

def is_vertical_reflection(c1, c2, flipped) :
	if c1 < 0 or c2 >= len(grid[0]) :
		return flipped
	
	for r in range(len(grid)) :
		if grid[r][c1] != grid[r][c2] and flipped:
			return False
		elif grid[r][c1] != grid[r][c2] :
			flipped = True
		
	return is_vertical_reflection(c1 - 1, c2 + 1, flipped)

grid = []
sum = 0
for l in open('input.txt') :
	l = l.strip()
	if l == '' :
		val = summarize(grid)
		sum += val
		grid = []
		continue
	grid.append(list(l))
sum += summarize(grid)
print(sum)