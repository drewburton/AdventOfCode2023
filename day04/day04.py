import fileinput
import re
import functools

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

cards = []
for line in fileinput.input(files="input.txt") :
	halves = line.split(' | ')
	parts = halves[0].split(' ')
	while not re.match('^\d+$', parts[0]) :
		parts.remove(parts[0])
	winning = set(map_to_int(parts))
	nums = map_to_int(halves[1].split(' '))
	matching = 0
	for num in nums :
		if num in winning :
			matching += 1
	cards.append([1, matching])

for i in range(len(cards)) :
	start = i + 1
	end = i + 1 + cards[i][1]
	for j in range(start, end) :
		cards[j] = [cards[j][0] + cards[i][0], cards[j][1]]
print(functools.reduce(lambda a, b : [a[0] + b[0], 0], cards)[0])