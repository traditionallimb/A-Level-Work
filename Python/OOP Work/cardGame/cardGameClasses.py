from random import shuffle


class Card:
	def __init__(self, cardRank: str, cardSuit: str):
		self.__cardRank = cardRank  # private
		self.__cardSuit = cardSuit  # private

	def print_name(self):
		print(f"{self.__cardRank} of {self.__cardSuit}")

	def get_suit(self):
		return self.__cardSuit

	def get_rank(self):
		return self.__cardRank


class Deck:
	def __init__(self, empty: bool):
		self.__cards = []  # private
		suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
		ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
		if not empty:
			for rank in ranks:
				for suit in suits:
					tempCard = Card(rank, suit)
					tempCardName = f"{tempCard.get_rank()} of {tempCard.get_suit()}"
					self.__cards.append(tempCardName)

	def get_size(self) -> int:
		return len(self.__cards)

	def deal_cards(self) -> str:
		topCard = self.__cards[0]
		self.__cards.pop(0)
		return topCard

	def add_card(self, cardToAdd: str):
		self.__cards.append(cardToAdd)

	def shuffle_deck(self):
		shuffle(self.__cards)

	def get_top_card(self) -> str:
		return self.__cards[0]

	def get_all(self) -> list:
		return self.__cards


class Player:
	def __init__(self):
		self.__playerHand = []

	def pick_up(self, playerDeck: list):
		self.__playerHand.append(playerDeck[0])
		playerDeck.pop(0)

	def get_hand(self) -> list:
		return self.__playerHand

	def get_hand_size(self) -> int:
		return len(self.__playerHand)
