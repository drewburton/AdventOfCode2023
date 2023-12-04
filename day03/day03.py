import fileinput
import re

schematic = []
sum = 0
nums = []
i = 0
for line in fileinput.input(files="input.txt") :
	matches = re.finditer('(\d+)', line)
	for match in matches :
		nums.append((i, match.start(), match.end(), match.group()))
	schematic.append([x for x in line])
	i += 1

symbol = '\d|\.|\n'
for num in nums :
	i, s, e, n = num
	n = int(n)
	contains_symbol = False
	for c in range(s - 1, e + 1) :
		if c < 0 or c >= len(schematic[0]) :
			continue
		if i - 1 >= 0 and not re.match(symbol, schematic[i - 1][c]):
			contains_symbol = True
			sum += n 
			break
		if i + 1 < len(schematic) and not re.match(symbol, schematic[i + 1][c]):
			contains_symbol = True
			sum += n
			break
	if not contains_symbol and s - 1 >= 0 and not re.match(symbol, schematic[i][s - 1]):
		contains_symbol = True
		sum += n
	if not contains_symbol and e < len(schematic[i]) and not re.match(symbol, schematic[i][e]):
		contains_symbol = True
		sum += n
print(sum)