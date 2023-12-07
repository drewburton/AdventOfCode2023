import fileinput
from functools import cmp_to_key

class Card :
	def __init__(self, cards, bid) :
		self.cards = cards
		self.bid = bid
		self.type = self.determine_type()

	def determine_type(self) :
		dict = {}
		for card in cards :
			if not dict.get(card) :
				dict[card] = 1
			else :
				dict[card] = dict[card] + 1
		t = None
		if len(dict) == 1 :
			t = 7	
		elif len(dict) == 2 :
			# four of a kind or full house
			c, count = next(iter(dict.items()))
			t = 6 if count == 4 or count == 1 else 5
		elif len(dict) == 3 :
			# three of a kind or two pair
			it = iter(dict.items())
			c, count = next(it)
			c, count2 = next(it)
			t = 4 if count == 3 or count2 == 3 or (count == 1 and count2 == 1) else 3
		elif len(dict) == 4 :
			t = 2
		else :
			t = 1

		if dict.get(1) :
			return self.handle_wilds(dict, t)
		return t
	
	def handle_wilds(self, dict, t) :
		if dict[1] == 1 :
			if t == 1 or t == 6 :
				return t + 1
			return t + 2
		if dict[1] == 2 :
			if t == 3 :
				return 6
			return t + 2
		if dict[1] == 3 :
			return t + 2
		if dict[1] == 4 :
			return t + 1
		return t


def compare(c1, c2) :
	if c1.type > c2.type :
		return 1
	if c1.type < c2.type :
		return -1
	for i in range(5) :
		if c1.cards[i] > c2.cards[i] :
			return 1
		if c1.cards[i] < c2.cards[i] :
			return -1
	return 0	

hands = []
for line in fileinput.input(files='input.txt') :
	parts = line.split(' ')
	cards = []
	for c in parts[0]:
		if c == 'T':
			cards.append(10)	
		elif c == 'J':
			cards.append(1)
		elif c == 'Q':
			cards.append(12)
		elif c == 'K':
			cards.append(13)
		elif c == 'A':
			cards.append(14)
		else :
			cards.append(int(c))
	bid = int(parts[1])
	hands.append(Card(cards, bid))

hands = sorted(hands, key=cmp_to_key(compare))

winning = 0
for i in range(len(hands)) :
	winning += hands[i].bid * (i + 1)
print(winning)