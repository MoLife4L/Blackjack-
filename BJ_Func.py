import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Deck:
    def __init__(self):
        self.cards = []
        self.deal_list = []
        self.player_list = []
        for suit in suits:
            for card in values:
                self.cards.append(card + " of " + suit)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        x = self.cards.pop()
        self.deal_list.append(x)
        return x

    def player_deal(self):
        x = self.cards.pop()
        self.player_list.append(x)
        return x


def player_input():
    choice = ''
    possible_choices = ['Y', 'y', 'n', 'N']
    while choice not in possible_choices:
        choice = input("Would you like to hit? Y or N: ")
    return choice.upper()


def current_count(cardlist):
    count = 0
    num_aces = 0  
    for card in cardlist:
        rank = card.split(" ")[0]
        count += values[rank]
        if rank == 'Ace':
            num_aces += 1
    while count > 21 and num_aces > 0:
        count -= 10
        num_aces -= 1
    return count


def replay():
    selections = ['y', 'Y', 'N', 'n']
    again = ''
    while again not in selections:
        again = input("Would you like to play again? (Y/N): ")
    return again.upper() == 'Y'
