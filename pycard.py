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
    def __init__(self, modifiers=None,
                 values=None,
                 text=None,
                 prFormat="DECKTXT of DECKMOD",
                 arr=None):
        """Deck(modifiers, values, text, prFormat) or Deck(prFormat, arr) Defaults: modifiers = [Hearts, Diamonds, Spades, Clubs] | values = [1, 2, ... 12, 13] | text = ["Ace", "Two", ... "Twelve", "Thirteen"] | prFormat = "DECKTXT of DECKMOD" """
        self.cards = []
        if values is None and arr is None:
            values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        if modifiers is None and arr is None:
            modifiers = ["Hearts", "Diamonds", "Spades", "Clubs"]
        if text is None and arr is None:
            text = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                    "King"]
        if text is None and values is None and modifiers is None and arr is not None:
            self.cards = arr
        self.format = prFormat
        self.hands = []
        self.unused = self.cards
        if arr is None:
            for i in range(len(values)):
                for modifier in modifiers:
                    self.cards.append((values[i], text[i], modifier))

    def printCardsStr(self, delimiter=", ", endlist='\n'):
        for i in range(len(self.cards)):
            card = self.cards[i]
            print(self.format.replace("DECKTXT", card[1]).replace("DECKMOD", card[2]).replace("DECKVAL", str(card[0])),
                  end='')
            if i != len(self.cards) - 1:
                print(delimiter, end='')
            else:
                print("", end=endlist)

    def getSingleStr(self, index):
        card = self.cards[index]
        return self.format.replace("DECKTXT", card[1]).replace("DECKMOD", card[2]).replace("DECKVAL", str(card[0]))

    def getSingleUnused(self, index):
        return self.unused[index]

    def shuffleUnused(self):
        shuffle(self.unused)

    def initPlayers(self, numPlayers):
        for i in range(numPlayers):
            self.hands.append([])

    def deal(self, numPlayers, numCards):
        for i in range(numPlayers):
            for j in range(numCards):
                self.hands[i].append(self.getSingleUnused(0))

    def compareVal(self, card1, card2):
        if card1[0] == card2[0]:
            return 0
        if card1[0] < card2[0]:
            return -1
        return 1

    def compareModifier(self, card1, card2):
        if card1[2] == card2[2]:
            return True
        else:
            return False

################
# BUTTON CLASS #
################
class Button:
    def __init__(self, size, position, image, screen):
        self.sz = size
        self.pos = position

    def getPos(self):
        return self.pos;

    def getSize(self):
        return self.sz

'''
TABLE OF CONTENTS:

Import Statements ........................ Line 5
Deck Class ............................... Line 11
Button Class .............................. Line 81

'''
