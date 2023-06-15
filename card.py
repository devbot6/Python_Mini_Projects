class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def value(self):
        if self.rank == 1:
            return 1
        elif self.rank in [11, 12, 13]:
            return 10
        else:
            return self.rank

    def __str__(self):
        ranks = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
                 11: "Jack", 12: "Queen", 13: "King"}
        suits = {"d": "Diamonds", "c": "Clubs", "h": "Hearts", "s": "Spades"}
        return f"{ranks[self.rank]} of {suits[self.suit]}"


import random

n = int(input("How many cards do you want to generate? "))

for i in range(n):
    rank = random.randint(1, 13)
    suit = random.choice(["d", "c", "h", "s"])
    card = Card(rank, suit)
    print(card, "- Blackjack value:", card.value())
