# Make a list of all the cards in a deck of cards that have hearts on them. 
# Your list would have items like ‘2 of Hearts’, ‘3 of Hearts’, ‘4 of Hearts’. 
# Do this efficiently by using a loop to generate as many cards as you can.

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

# Loop through your list and print out all of the cards in order.
	print("All our heart cards printed as strings: ")
	for item, value in enumerate(deck):
		print(f"Card number: {item + 1} -->", value)

# Loop through a slice of your list and print out just the cards with numbers on them.
	print("Here are the heart cards with only numbers: ")
	for value, item in enumerate(deck):
		if value == 9:
			break
		print(f"Card number: {value + 1} -->", item)

# Loop through a slice of your list and print out just the face cards.
	print("Here are the heart cards with faces on them: ")
	for value, item in enumerate(deck):
		if value <= 8:
			continue
		print(f"Card number: {value + 1} -->", item)

Creating_deck()