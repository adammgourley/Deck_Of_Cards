# deck.py

import random

class Deck:
	suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
	values = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

	def __init__(self):
		self.deck = []
		self.get_deck()

	def get_deck(self):
		self.deck = []
		for s in Deck.suits:
			for v in Deck.values:
				self.deck.append(f"{str(v)} of {s}")
		return self.shuffle(self.deck)

	def shuffle(self, deck):
		random.shuffle(deck)
		return deck

	def draw(self):
		card = self.deck.pop()
		return card