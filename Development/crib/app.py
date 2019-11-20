# Author: Stephen Scott
# Date: November 19, 2019


import random
import numpy as np


class Card:
    def __init__(self):
        self.num = random.randint(2, 14)
        self.suit = random.randint(1, 4)


class Hand:
    def __init__(self, handSize):
        self.handSize = handSize
        self.cards = []
        self.cardsInHand = np.zeros((4, 13))

    def getHandSize(self):
        print(self.handSize)

    def createHand(self):
        for i in range(self.handSize):
            card = Card()
            while self.cardsInHand[card.suit - 1][card.num - 2] == 1:
                card = Card()
            self.cardsInHand[card.suit - 1][card.num - 2] += 1
            self.cards.append(card)

    def viewHand(self):
        for i in range(self.handSize):
            if self.cards[i].suit == 1:
                if self.cards[i].num == 11:
                    print("Suit:\tClubs\t\t\tValue:\tJack")
                elif self.cards[i].num == 12:
                    print("Suit:\tClubs\t\t\tValue:\tQueen")
                elif self.cards[i].num == 13:
                    print("Suit:\tClubs\t\t\tValue:\tKing")
                elif self.cards[i].num == 14:
                    print("Suit:\tClubs\t\t\tValue:\tAce")
                else:
                    print("Suit:\tClubs\t\t\tValue:\t", self.cards[i].num)

            elif self.cards[i].suit == 2:
                if self.cards[i].num == 11:
                    print("Suit:\tDiamonds\t\tValue:\tJack")
                elif self.cards[i].num == 12:
                    print("Suit:\tDiamonds\t\tValue:\tQueen")
                elif self.cards[i].num == 13:
                    print("Suit:\tDiamonds\t\tValue:\tKing")
                elif self.cards[i].num == 14:
                    print("Suit:\tDiamonds\t\tValue:\tAce")
                else:
                    print("Suit:\tDiamonds\t\tValue:\t", self.cards[i].num)
            elif self.cards[i].suit == 3:
                if self.cards[i].num == 11:
                    print("Suit:\tHearts\t\t\tValue:\tJack")
                elif self.cards[i].num == 12:
                    print("Suit:\tHearts\t\t\tValue:\tQueen")
                elif self.cards[i].num == 13:
                    print("Suit:\tHearts\t\t\tValue:\tKing")
                elif self.cards[i].num == 14:
                    print("Suit:\tHearts\t\t\tValue:\tAce")
                else:
                    print("Suit:\tHearts\t\t\tValue:\t", self.cards[i].num)
            else:
                if self.cards[i].num == 11:
                    print("Suit:\tSpades\t\t\tValue:\tJack")
                elif self.cards[i].num == 12:
                    print("Suit:\tSpades\t\t\tValue:\tQueen")
                elif self.cards[i].num == 13:
                    print("Suit:\tSpades\t\t\tValue:\tKing")
                elif self.cards[i].num == 14:
                    print("Suit:\tSpades\t\t\tValue:\tAce")
                else:
                    print("Suit:\tSpades\t\t\tValue:\t", self.cards[i].num)


def main():
    newHand = Hand(52)
    newHand.getHandSize()
    newHand.createHand()
    newHand.viewHand()
    print(newHand.cardsInHand)


main()
