#Justine Moturi
#purpose: Deck card
#date:October 20th 2022
from random import randint
from CardDeck.card import Card

class Deck:
    def __init__(self):
        self.card_list = []

    #adds cards to the Deck stored in the address cardlist
    def add_standard_cards(self):
        for suit in range(1,5):
            for number in range(1,14):
                card = Card(number, suit)
                self.card_list.append(card)

    # shuffles the cards in a random order

    def shuffle(self):
        for position in range(0,len(self.card_list)):
            swap_to = randint(0, 51)
    # swaps cards based on position
            self.card_list[position], self.card_list[swap_to] = self.card_list[swap_to], self.card_list[position]

    # Takes a parameter number and creates a hand deck

    def deal(self, number):
        hand = Deck()

    # remove cards from standard deck and put them into the new hand
        for i in range(number):
            hand.card_list.append(self.card_list.pop(i))

        return hand







