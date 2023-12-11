import fileinput

def extrapolate(list) :
	extrapolation = [list]

	num_set = set()
	while len(num_set) != 1 or 0 not in num_set:
		num_set = set()
		next = []
		for i in range(len(extrapolation[-1]) - 1) :
			val = extrapolation[-1][i + 1] - extrapolation[-1][i]
			next.append(val)
			num_set.add(val)
		extrapolation.append(next)	
	return extrapolation

def getNextValue(extrapolation) :
	extrapolation[-1].insert(0, 0)
	for i in range(len(extrapolation) - 2, -1, -1) :
		extrapolation[i].insert(0, extrapolation[i][0] - extrapolation[i + 1][0])	
	return extrapolation[0][0]

sum = 0
for line in fileinput.input(files='input.txt') :
	extrapolation = extrapolate([int(x) for x in line.split(' ')])
	sum += getNextValue(extrapolation)
print(sum)