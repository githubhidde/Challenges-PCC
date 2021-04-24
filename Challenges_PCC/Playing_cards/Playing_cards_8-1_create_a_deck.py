# Write a function called build_deck(). This function takes no arguments,
# and returns a list containing all the cards in a standard deck, in order.

def Creating_deck():
	cards = []
	suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
	royals = ["Jack", "Queen", "King", "Ace"]
	deck = []
	for i in range(2, 11):
		cards.append(str(i))

# Added the royals to to list
	for r in range(4):
		cards.append(royals[r])

# Now we attach the suits
	for r in range(4):
		for c in range(13):
			card = (cards[c] + " of " + suits[r])
			# Let's add the cards to the deck
			deck.append(card)

	print("All our cards in the deck printed as strings: ")
	for item, value in enumerate(deck):
		print(f"Card number: {item + 1} -->", value)

Creating_deck()