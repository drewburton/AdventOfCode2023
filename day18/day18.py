from enum import IntEnum
from itertools import pairwise
import re

def shoelace(outline) :
	return abs(sum(row1 * col2 - col1 * row2 for (row1, col1), (row2, col2) in pairwise(outline)) / 2)

def picks(num_points, area) :
	return int(area - 0.5 * num_points + 1 + num_points)

pattern = re.compile('([RUDL]) (\d+) \((.*)\)')
outline = []
current = (0, 0)
outline.append(current)
for l in open('input.txt') :
	match = re.match(pattern, l)
	direction = match.group(1)
	magnitude = int(match.group(2))
	color = match.group(3)

	r, c = outline[-1]
	if direction == 'U' :
		for i in range(magnitude) :
			outline.append((r - (i + 1), c))
	elif direction == 'D' :
		for i in range(magnitude) :
			outline.append((r + i + 1, c))
	elif direction == 'L' :
		for i in range(magnitude) :
			outline.append((r, c - (i + 1)))
	else :
		for i in range(magnitude) :
			outline.append((r, c + i + 1))

outline = outline[:-1]
area = shoelace(outline)
points = picks(len(outline), area)
print(points)