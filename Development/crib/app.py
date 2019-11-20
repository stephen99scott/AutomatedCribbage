# Author: Stephen Scott
# Date: November 19, 2019
# Description: Used to analyze an input hand of cards and output a cribbage score
# Filename: app.py


import random
import numpy as np


class Card:
    def __init__(self, num=0, suit=0):
        self.num = num
        self.suit = suit


class Hand:
    def __init__(self, handSize):
        self.handSize = handSize
        self.cards = []
        self.cardsInHand = np.zeros((4, 13))

    def deleteHand(self):
        self.handSize = 0
        self.cards = []
        self.cardsInHand = np.zeros((4, 13))

    def getHandSize(self):
        print(self.handSize)

    def generateHand(self):
        for i in range(self.handSize):
            card = Card()
            card.num = random.randint(2, 14)
            card.suit = random.randint(1, 4)
            while self.cardsInHand[card.suit - 1][card.num - 2] == 1:
                card = Card()
                card.num = random.randint(2, 14)
                card.suit = random.randint(1, 4)
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
        print(self.cardsInHand)

    def sendHand(self, cardsSent=[]):
        for card in cardsSent:
            if card.num > 14 or card.num < 2 or card.suit > 4 or card.suit < 1:
                print("###CARD NUM OR SUIT EXCEEDS RANGE###")
                self.deleteHand()
                print("########HAND NOT INITIALIZED########")
                return
            elif self.cardsInHand[card.suit - 1][card.num - 2] == 1:
                print("######DUPLICATE CARD NOT ADDED######")
                self.deleteHand()
                print("########HAND NOT INITIALIZED########")
                return
            else:
                self.cardsInHand[card.suit - 1][card.num - 2] += 1
                self.cards.append(card)


def main():
    cards = [Card(14, 4), Card(3, 3), Card(4, 2), Card(6, 1)]
    test = Hand(len(cards))
    test.sendHand(cards)
    test.getHandSize()
    test.viewHand()


main()
