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
        self.cardsInHand = np.zeros((4, 13))  # Counts the instances of each card
        self.handSize = handSize  # Init the hand with a size
        self.cards = []  # Init empty array of card objects
        self.nums = []  # Init empty array of card.num values
        self.numOfSuit = np.zeros(4)  # Counts the instances of each suit
        self.score = 0  # Final output score from a hand

    def deleteHand(self):
        self.handSize = 0
        self.cards = []
        self.cardsInHand = np.zeros((4, 13))

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
            self.nums.append(card.num)
            self.numOfSuit[card.suit - 1] += 1

    def viewHand(self):
        suit_names = ["", "Clubs", "Diamonds", "Hearts", "Spades"]
        card_names = ["", "", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for i in range(self.handSize):
            print("Value:\t" + card_names[self.cards[i].num] + "\t\t\tSuit:\t" + suit_names[self.cards[i].suit])
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
                self.nums.append(card.num)
                self.numOfSuit[card.suit - 1] += 1

    def scoreHand(self):
        # If 4 or more of one suit in a hand, then add 4 or more to the score
        for num in self.numOfSuit:
            if num < 4:
                continue
            else:
                self.score += int(num)
        # For each combination of 15 in a hand, add 2 to score
        # some code
        # If 3 or more consecutive nums in a hand, add 3 or more to score
        # some code
        # If pair of num in hand, add 2, if 3pair add 6, if 4pair add 12
        # some code


def main():
    cards = [Card(14, 2), Card(5, 2), Card(8, 2), Card(9, 2)]
    test = Hand(len(cards))
    test.sendHand(cards)
    test.viewHand()
    test.scoreHand()
    print(test.score)


main()
