import random


class Card:
    VALUE = {'ACE': 1, '2': 2, '3': 3, '4': 4, '5': 5,
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



class Deck:
    SUIT = ['CLUBS', 'SPADES', 'HEARTS', 'DIAMONDS']
    RANK = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']

    def __init__(self):
        self.new_deck()

    def new_deck(self):
        self.deck = []
        for s in self.SUIT:
            for r in self.RANK:
                self.deck.append(Card(s, r))

        # ...is the same as this... This is called a List Comprehension

        self.deck = [Card(s, r) for s in self.SUIT for r in self.RANK]

    def print_deck(self):
        for card in self.deck:
            card.print_card()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        card = self.deck.pop()
        return card


if __name__ == '__main__':

    deck = Deck()
    print('my deck')
    deck.print_deck()

    print('\n\nshuffled deck')
    deck.shuffle()
    deck.print_deck()

    print('\n\npick cards')
    for h in range(3):
        print('\nhand', h + 1)
        for i in range(5):
            card = deck.deal_card()
            card.print_card()
