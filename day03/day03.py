import fileinput
import re

class Num :
	def __init__(self, num, row, start, end) :
		self.num = num
		self.row = row
		self.start = start
		self.end = end
		self.gear = ()

schematic = []
nums = []
gears = []
i = 0
for line in fileinput.input(files="input.txt") :
	nums_matches = re.finditer('(\d+)', line)
	gear_matches = re.finditer('(\*)', line)
	for match in nums_matches :
		nums.append(Num(int(match.group()), i, match.start(), match.end()))
	for match in gear_matches :
		gears.append((i, match.start()))
	schematic.append([x for x in line])
	i += 1

gear = '\*'
for num in nums :
	i = num.row
	s = num.start
	e = num.end
	n = num.num
	contains_gear = False
	for c in range(s - 1, e + 1) :
		if c < 0 or c >= len(schematic[0]) :
			continue
		if i - 1 >= 0 and re.match(gear, schematic[i - 1][c]):
			contains_gear = True
			num.gear = (i-1, c)
			break
		if i + 1 < len(schematic) and re.match(gear, schematic[i + 1][c]):
			contains_gear = True
			num.gear = (i + 1, c)
			break
	if not contains_gear and s - 1 >= 0 and re.match(gear, schematic[i][s - 1]):
		contains_gear = True
		num.gear = (i, s - 1)
	if not contains_gear and e < len(schematic[i]) and re.match(gear, schematic[i][e]):
		contains_gear = True
		num.gear = (i, e)

sum = 0
for gear in gears :
	parts = list(map(lambda n : n.num, list(filter(lambda n : n.gear == gear, nums))))
	if len(parts) != 2 :
		continue
	sum += parts[0] * parts[1]
print(sum)

