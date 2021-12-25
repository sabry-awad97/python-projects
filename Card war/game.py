from deck import Deck
from player import Player


class Game:
    def __init__(self):
        name1 = "A"  # input("Enter player 1 name: ")
        name2 = "B"  # input("Enter player 2 name: ")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def play_game(self):
        cards = self.deck.cards
        print("Beginning War")
        response = None
        while len(cards) >= 2 and response != 'q':
            response = input('q to quit. Any other key to play.')
            player1_card = self.deck.remove_card()
            player2_card = self.deck.remove_card()
            print("{} drew {}, {} drew {}"
                  .format(self.player1.name, player1_card, self.player2.name, player2_card))
            if player1_card > player2_card:
                self.player1.wins += 1
                print("{} wins this round".format(self.player1.name))
            else:
                self.player2.wins += 1
                print("{} wins this round".format(self.player2.name))

    @property
    def winner(self):
        if self.player1.wins > self.player2.wins:
            return f"{self.player1.name} wins with {self.player1.wins}"

        if self.player1.wins < self.player2.wins:
            return f"{self.player2.name} wins with {self.player2.wins}"
        return f"It was a tie! with {self.player1.wins}"
