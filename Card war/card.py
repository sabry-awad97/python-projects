class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    ranks = [None, None,
             "2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King", "Ace"]

    def __init__(self, rank, suit):
        """
        :type rank: int
        :type suit: int
        """
        self.rank = rank
        self.suit = suit

    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        elif self.rank == other.rank:
            return self.suit < other.suit
        else:
            return False

    def __repr__(self):
        return self.ranks[self.rank] + " of " + self.suits[self.suit]
