import re

cache = {}

def count_arrangements(spring, pattern) :

	if spring == '' :
		return 1 if pattern	== () else 0

	if pattern == () :
		return 0 if '#' in spring else 1

	key = (spring, pattern)
	if key in cache :
		return cache[key]

	result = 0
	# treat ? as a . and skip dots	
	if spring[0] in '.?' :
		result += count_arrangements(spring[1:], pattern)	

	# treat ? as a # if it fits in the block
	if spring[0] in '#?' :
		# case 1: can't require more than is left in the spring
		# case 2: can't create the block if there is a . from here to the length of the block
		# case 3: can't have the next one after the block be #
		if pattern[0] <= len(spring) and '.' not in spring[:pattern[0]] and (pattern[0] == len(spring) or '#' != spring[pattern[0]]) :
			result += count_arrangements(spring[pattern[0] + 1:], pattern[1:])

	# store the result for this state so we don't repeat calculations
	cache[(spring, pattern)] = result
	return result

def unfold(spring, pattern) :
	return (('?'.join([spring] * 5)), (','.join([pattern] * 5)))

sum = 0
for l in open('input.txt') :
	parts = l.split(' ')
	spring = parts[0]
	pattern = parts[1]
	if pattern[-1] == '\n' :
		pattern = pattern[:-1]

	spring, pattern = unfold(spring, pattern)
	pattern = tuple(map(int, pattern.split(',')))
	sum += count_arrangements(spring, pattern)	

print(sum)