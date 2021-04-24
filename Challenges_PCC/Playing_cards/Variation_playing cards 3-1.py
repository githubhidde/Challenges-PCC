# Cards are typically divided into four suits (clubs, hearts, spades, diamonds) 
# Two colors (red and black)
# Face cards and number cards.

# First things first, we just import a card set
# i'm not about to create it myself for this time.
from collections import namedtuple

Card = namedtuple('Card', ['value', 'suit'])
suits = ['hearts', 'diamonds', 'spades', 'clubs']
cards = [Card(value, suit) for value in range(1, 14) for suit in suits]

# The cards which consist hearts should be appended to an empty list
deck_of_hearts = []

def Deck_of_hearts():
# Make a list of cards that have hearts on them
	for item, value in enumerate(cards):
# Search in the list for the keyword 'hearts'
		if 'hearts' in value:
			deck_of_hearts.append(value)
# The heart cards should be added to the list.
# Let's print the list and show the heart cards
# Actually, printing the first 3 cards is adequate
	print(deck_of_hearts[0:3])
	print("As you see there are the first three cards with hearts on them from the deck, going from 1 through 3.")

Deck_of_hearts()