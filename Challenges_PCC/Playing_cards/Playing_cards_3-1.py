# A standard deck of cards has four suites: hearts, clubs, spades, diamonds. 
# Each suite has thirteen cards: 
# ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen and king

cards = []
suits = ['Hearts']
royals = ["Jack", "Queen", "King", "Ace"]
deck = []

# We start with adding the numbers 2 through 10.
# Since there are only 4 royals and 9 'regular card'
# Which makes 13 card in total per suit.
def Creating_deck():
	for i in range(2, 11):
		cards.append(str(i))

# Added the roys to to list
	for r in range(4):
		cards.append(royals[r])

# Now we attach the suits
	for r in range(1):
		for c in range(13):
			card = (cards[c] + " of " + suits[r])
			# Let's add the cards to the deck
			deck.append(card)
	# Perfect we have a full deck of cards
	# print(deck)
	# Now we get to the actual assignment, namely printing the list 
	# and show the heart cards
	# Actually, only printing the first 3 cards is already adequate
	print("The first 3 items in the list:", deck[:3])
	# You can print them as 'strings' as well:
	print("The first 3 cards printed as strings: ")
	for item, value in enumerate(deck):
		if item == 3:
			break
		print(value)

Creating_deck()