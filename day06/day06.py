import fileinput
import math
import re

reader = fileinput.input(files='input.txt')
time = int(''.join(re.findall('(\d+)', reader.readline())))
distance = int(''.join(re.findall('(\d+)', reader.readline())))

speed = 1
travelTime = math.ceil((distance + 1) / speed)
wins = 0
while speed <= time :
	speed += 1
	travelTime = math.ceil((distance + 1) / speed)
	if (speed + travelTime <= time) :
		wins += 1
print(wins)