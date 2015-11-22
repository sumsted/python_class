class Card:

    VALUE = {
        'ACE': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'JACK': 11, 'QUEEN': 12, 'KING': 13
    }

    def __init__(self, suit, rank):
        self.suit = suit.upper()
        self.rank = rank.upper()

    def print_card(self):
        print(self.rank, 'of', self.suit)

    def __lt__(self, other):
        if self.VALUE[other.rank] < self.VALUE[self.rank]:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.VALUE[other.rank] == self.VALUE[self.rank]



if __name__ == '__main__':
    ac = Card('CLUBS', 'ACE')
    th = Card('HEARTS', '10')
    print(ac > th)

    ts = Card('SPADES', '10')
    print(ts == th)
    print(ac == th)
