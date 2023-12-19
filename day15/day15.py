def hash(s) :
	result = 0
	for c in s :
		result += ord(c)
		result *= 17
	return result % 256

def parse_lens(inp) :
	if '-' in inp :
		remove(inp)
	else :
		update(inp)
		
def remove(inp) :
	label = inp[:-1]
	box = hash(label)
	if box not in boxes.keys() :
		return
	for i in range(len(boxes[box])) :
		l, f = boxes[box][i]
		if l == label :
			boxes[box].pop(i)	
			break

def update(inp) :
	parts = inp.split('=')
	label = parts[0]
	focal = int(parts[1])
	box = hash(label)
	found = False
	if box not in boxes.keys() :
		boxes[box] = [(label, focal)]
		return
	for i in range(len(boxes[box])) :
		l, f = boxes[box][i]
		if l == label :
			boxes[box][i] = (label, focal)
			found = True
			break
	if not found :
		boxes[box].append((label, focal))

def focusing_power() :
	total = 0
	for key in boxes.keys() :
		for i in range(len(boxes[key])) :
			l, f = boxes[key][i]
			total += (key + 1) * (i + 1) * f
	return total

boxes = {}
for l in open('input.txt') :
	steps = l.split(',')
	for step in steps :
		parse_lens(step)

print(focusing_power())

