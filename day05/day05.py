import fileinput

class Map :
	def __init__(self) :
		self.range = []

	def mapping(self, num) :
		for r in self.range :
			result = r.mapping(num)
			if result != num :
				break
		return result

class Range :
	def __init__(self, dest, source, range) :
		self.dest = dest
		self.source = source
		self.range = range
	
	def __str__(self) :
		return str(self.dest) + " " + str(self.source) + " " + str(self.range)
	
	def mapping(self, num) :
		if num >= self.source and num <= self.source + self.range:
			return (num - self.source) + self.dest
		return num

seeds = []
seed_to_soil = Map()
soil_to_fertilizer = Map()
fertilizer_to_water = Map()
water_to_light = Map()
light_to_temperature = Map()
temperature_to_humidity = Map()
humidity_to_location = Map()
inputMap = {
	"seed-to-soil map:" : seed_to_soil,
	"soil-to-fertilizer map:" : soil_to_fertilizer,
	"fertilizer-to-water map:" :fertilizer_to_water,
	"water-to-light map:" : water_to_light,
	"light-to-temperature map:" : light_to_temperature,
	"temperature-to-humidity map:" : temperature_to_humidity,
	"humidity-to-location map:" : humidity_to_location
}
currentInput = None
for line in fileinput.input(files="input.txt") :
	if line == '\n':
		continue
	line = line.strip()
	if line.startswith('seeds:') :
		line = line.replace('seeds: ', '')
		temp = [int(x) for x in line.split(' ')]
		for i in range(0, len(temp), 2) :
			for val in [x for x in range(temp[i], temp[i] + temp[i + 1])] :
				seeds.append(val)
	elif not line[0].isdigit() :
		currentInput = inputMap.get(line)
	else :
		dest, source, range = (int(x) for x in line.split(' '))
		map = Range(dest, source, range)
		currentInput.range.append(map)

min_loc = float('inf')
for seed in seeds :
	soil = seed_to_soil.mapping(seed)
	fertilizer = soil_to_fertilizer.mapping(soil)
	water = fertilizer_to_water.mapping(fertilizer)
	light = water_to_light.mapping(water)
	temp = light_to_temperature.mapping(light)
	humidity = temperature_to_humidity.mapping(temp)
	location = humidity_to_location.mapping(humidity)
	min_loc = min(min_loc, location)
print(min_loc)	
