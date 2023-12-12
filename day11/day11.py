with open('input.txt') as f :
	def expand(galaxies) :
		expansion = 1000000 - 1
		row_set = set()
		col_set = set()
		maxr = float('-inf')
		maxc = float('-inf')
		for galaxy in galaxies :
			r, c = galaxy
			maxr = max(maxr, r)
			maxc = max(maxc, c)
			row_set.add(r)
			col_set.add(c)
		i = 0
		while i <= maxr :
			if i not in row_set :
				galaxy_list = list(galaxies)
				for g in range(len(galaxy_list)) :
					r, c = galaxy_list[g]
					galaxy_list[g] = (r + expansion if r > i else r, c)
				galaxies = set(galaxy_list)
				maxr += expansion
				row_set = set((x + expansion for x in row_set))
				i += expansion
			i += 1
		j = 0
		while j <= maxc :
			if j not in col_set :
				galaxy_list = list(galaxies)	
				for g in range(len(galaxy_list)) :
					r, c = galaxy_list[g]
					galaxy_list[g] = (r, c + expansion if c > j else c)
				galaxies = set(galaxy_list)
				maxc += expansion
				col_set = set((x + expansion for x in col_set))
				j += expansion
			j += 1
		return galaxies

	def sum_paths(galaxies) :
		sum = 0
		for g1 in galaxies :
			for g2 in galaxies :
				if g1 <= g2 :
					continue
				sum += shortest(g1, g2)
		return sum

	def shortest(g1, g2) :
		r1, c1 = g1
		r2, c2 = g2
		return abs(c2 - c1) + abs(r2 - r1)

	galaxies = set()
	i = 0
	for l in f :
		for j in range(len(l)) :
			if l[j] == '#' :
				galaxies.add((i, j))
		i += 1
	galaxies = expand(galaxies)
	print(sum_paths(galaxies))