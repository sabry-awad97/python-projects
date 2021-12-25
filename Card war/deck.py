from random import shuffle
from card import Card


class Deck:
    def __init__(self):
        self.cards = [Card(i, j) for i in range(2, 15) for j in range(4)]
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
