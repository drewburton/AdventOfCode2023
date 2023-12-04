import fileinput
import re

def map_to_int(arr) :
	to_remove = []
	for i in range(len(arr)) :
		if arr[i] == '' :
			to_remove.append(arr[i])
			continue
		if arr[i].endswith('\n') :
			arr[i].replace('\n', '')
		arr[i] = int(arr[i])
	return [i for i in arr if i not in to_remove]

total = 0
for line in fileinput.input(files="input.txt") :
	halves = line.split(' | ')
	parts = halves[0].split(' ')
	while not re.match('^\d+$', parts[0]) :
		parts.remove(parts[0])
	winning = set(map_to_int(parts))
	nums = map_to_int(halves[1].split(' '))
	points = 0
	for num in nums :
		if num in winning :
			points = 1 if points == 0 else 2 * points
	total += points
print(total)