from dataclasses import dataclass
from enum import IntEnum
import heapq

class Direction(IntEnum) :
	UP = 0
	RIGHT = 1
	DOWN = 2
	LEFT = 3

	@staticmethod
	def rotate(direction, type) :
		return Direction((direction + (1 if type == 'CW' else -1)) % 4)

	@staticmethod
	def move(direction) :
		if direction == Direction.UP :
			return (-1, 0)
		if direction == Direction.RIGHT :
			return (0, 1)
		if direction == Direction.DOWN :
			return (1, 0)
		if direction == Direction.LEFT :
			return (0, -1)

@dataclass(frozen=True, order=True)
class Pos:
	r: int
	c: int
	dir: Direction

def is_valid_move(r, c) :
	if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) :
		return True

grid = []
for l in open('input.txt') :
	grid.append(list(map(int, l.strip())))

seen = set()

queue = []
queue.append((0, Pos(0, 0, Direction.RIGHT), 0))
queue.append((0, Pos(0, 0, Direction.DOWN), 0))

while queue :
	cost, pos, steps = heapq.heappop(queue)

	if pos.r == len(grid) - 1 and pos.c == len(grid[0]) -1 :
		print(cost)
		break

	if (pos, steps) in seen :
		continue
	seen.add((pos, steps))

	# turn left and step
	d = Direction.rotate(pos.dir, "CCW")
	r, c = Direction.move(d)
	r += pos.r
	c += pos.c
	move = Pos(r, c, d)
	if is_valid_move(r, c) :
		heapq.heappush(queue, (cost + grid[r][c], move, 1))

	# turn right and step
	d = Direction.rotate(pos.dir, "CW")
	r, c = Direction.move(d)
	r += pos.r
	c += pos.c
	move = Pos(r, c, d)
	if is_valid_move(r, c) :
		heapq.heappush(queue, (cost + grid[r][c], move, 1))

	# continue forward if steps < 3
	r, c = Direction.move(pos.dir)
	r += pos.r
	c += pos.c
	move = Pos(r, c, pos.dir)
	if steps < 3 and is_valid_move(r, c):
		heapq.heappush(queue, (cost + grid[r][c], move, steps + 1))