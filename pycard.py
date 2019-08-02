'''
TABLE OF CONTENTS IS ON BOTTOM LINE
'''

#####################
# IMPORT STATEMENTS #
#####################
from random import shuffle

##############
# DECK CLASS #
##############
class Deck:
    def __init__(self, modifiers = ["Hearts", "Diamonds", "Spades", "Clubs"], values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], text = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"], prFormat = "DECKTXT of DECKMOD"):
        self.cards = []
        self.format = prFormat
        self.hands = []
        self.unused = self.cards
        for i in range(len(values)):
            for modifier in modifiers:
                self.cards.append((values[i], text[i], modifier))

    def printCardsStr(self, delimiter = ", ", endlist = '\n'):
        for i in range(len(self.cards)):
            card = self.cards[i]
            print(self.format.replace("DECKTXT", card[1]).replace("DECKMOD", card[2]).replace("DECKVAL", str(card[0])), end='')
            if i != len(self.cards) - 1:
                print(delimiter, end='')
            else:
                print("", end = endlist)

    def printSingleStr(self, index):
        card = self.cards[index]
        print(self.format.replace("DECKTXT", card[1]).replace("DECKMOD", card[2]).replace("DECKVAL", str(card[0])))

    def getSingleStr(self, index):
        card = self.cards[index]
        return (self.format.replace("DECKTXT", card[1]).replace("DECKMOD", card[2]).replace("DECKVAL", str(card[0])))

    def getSingleUnused(self, index):
        #TODO: implement
        pass

    def shuffleUnused(self, index):
        #TODO: implement
        pass

'''
TABLE OF CONTENTS:

Import Statements ........................ Line 5
Deck Class ............................... Line 10
Button Clas .............................. Line #

'''