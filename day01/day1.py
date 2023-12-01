import fileinput
import re

nums = {
	"one" : 1,
	"two" : 2,
	"three" : 3,
	"four" : 4,
	"five" : 5, 
	"six" : 6,
	"seven" : 7,
	"eight" : 8,
	"nine" : 9
}

regex = '(\d|one|two|three|four|five|six|seven|eight|nine)'
reverse_regex = '(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)'
sum = 0
for line in fileinput.input(files='input.txt') :
	first = re.search(regex, line)
	first = str(nums.get(first[0]) or int(first[0]))
	second = re.search(reverse_regex, line[::-1])
	second = str(nums.get(second[0][::-1]) or int(second[0]))
	sum += int(first + second)
print(sum)
