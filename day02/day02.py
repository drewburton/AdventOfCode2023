import fileinput
import re

sum = 0
for line in fileinput.input(files='input.txt') :
	parts = line.split('; ')
	id = int(re.search('(\d+)', parts[0]).group(0))
	parts[0] = parts[0].split(':')[1][1:]
	max_red = float('-inf')
	max_blue = float('-inf')
	max_green = float('-inf')
	for part in parts :
		matches = re.findall('(\d+) (red|blue|green)', part)
		for match in matches :
			amount, color = match
			amount = int(amount)
			if color == 'red':
				max_red = max(max_red, amount)
			elif color == 'blue' :
				max_blue = max(max_blue, amount)
			elif color == 'green' :
				max_green = max(max_green, amount)
	sum += max_red * max_blue * max_green
print(sum)