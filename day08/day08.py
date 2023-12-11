import fileinput
import math
import re 

node_map = {}
input = fileinput.input(files='input.txt')
navigation = input.readline().strip()
input.readline()
for line in input:
	matches = re.findall('([1-9A-Z]{3})', line)
	node_map[matches[0]] = (matches[1], matches[2])

current_nodes = [x for x in node_map.keys() if x.endswith('A')]
i = 0
multiples = []
while False in [True if x.endswith('Z') else False for x in current_nodes] :
	direction = navigation[i % len(navigation)]
	if direction == 'L' :
		current_nodes = [node_map[x][0] for x in current_nodes]
	else :
		current_nodes = [node_map[x][1] for x in current_nodes]

	i += 1

	for j in range(len(current_nodes)) :
		if j < len(current_nodes) and current_nodes[j].endswith('Z') :
			current_nodes.remove(current_nodes[j])
			multiples.append(i)

print(math.lcm(*multiples))
