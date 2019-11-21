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
        # If 4 or more of a suit in a hand then add 4 or more to score
        for num in self.numOfSuit:
            if num < 4:
                continue
            else:
                self.score += int(num)
        self.nums.sort()  # Sort the value of the cards
        currentRun = 1
        maxRun = 1
        multiplier = 1
        pairs = 0
        for num in range(self.handSize):
            if num + 1 < self.handSize:
                if self.nums[num] == 2 and self.nums[self.handSize - 1] == 14:
                    currentRun = 2
                if self.nums[num + 1] == self.nums[num]:
                    multiplier += 1
                    pairs += 1
                else:
                    if pairs == 1:
                        self.score += 2
                    elif pairs == 2:
                        self.score += 6
                    elif pairs == 3:
                        self.score += 12
                    pairs = 0
                if self.nums[num + 1] == self.nums[num] + 1:
                    currentRun += 1
                else:
                    currentRun = 1
            if currentRun > maxRun:
                maxRun = currentRun
        if maxRun > 2:
            self.score += maxRun * multiplier


def main():
    cards = [Card(3, 2), Card(3, 3), Card(3, 4), Card(4, 2), Card(5, 4)]
    test = Hand(len(cards))
    test.sendHand(cards)
    test.viewHand()
    test.scoreHand()
    print(test.score)


main()
