from cardGameClasses import *

mainDeck = Deck(False)
computerDeck = Deck(True)
userDeck = Deck(True)

mainDeck.shuffle_deck()

for i in range(24):
	computerDeck.add_card(mainDeck.deal_cards())
	userDeck.add_card(mainDeck.deal_cards())

computer = Player()
user = Player()

for i in range(5):
	computer.pick_up(computerDeck.get_all())
	user.pick_up(userDeck.get_all())

topCard = mainDeck.get_top_card()

print(mainDeck.get_all())
print(computerDeck.get_all())
print(userDeck.get_all())
print(user.get_hand())
print(computer.get_hand())
print(topCard)


checkParams = [user.get_hand_size() != 0 and userDeck.get_size() != 0,
			   computer.get_hand_size() != 0 and computerDeck.get_size() != 0,
			   userDeck.get_size() != 0 and computerDeck.get_size() != 0]

while all(checkParams):
	user



