# Author: Stephen Scott
# Date: November 19, 2019
# Description: Used to analyze an input hand of cards and output a cribbage score
# Filename: app.py


import random
import numpy as np
import matplotlib.pyplot as plt


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
        self.sortedNums = []  # Init empty array to hold sorted nums
        self.sortedNumsReducedFaceValue = []  # Make face cards have a value of 10, aces have a value of 1
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
            print("Card:\t" + card_names[self.cards[i].num] + ", " + suit_names[self.cards[i].suit])

    def viewDeck(self):
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

    def sortNums(self):
        for num in range(self.handSize):
            self.sortedNums.append(self.nums[num])
        self.sortedNums.sort()

    def reduceFaceValue(self):
        for num in range(self.handSize):
            if self.nums[num] == 14:
                self.sortedNumsReducedFaceValue.append(1)
            elif 14 > self.nums[num] > 10:
                self.sortedNumsReducedFaceValue.append(10)
            else:
                self.sortedNumsReducedFaceValue.append(self.nums[num])
        self.sortedNumsReducedFaceValue.sort()

    def checkPairs(self):
        pairs = 0
        for num in range(self.handSize - 1):
            if self.sortedNums[num + 1] == self.sortedNums[num]:
                pairs += 1
            else:
                self.score = self.score + pairs * (pairs + 1)
                pairs = 0
        self.score = self.score + pairs * (pairs + 1)

    def checkFlush(self):
        for num in self.numOfSuit:
            if num < 4:
                continue
            else:
                self.score += int(num)

    def checkRuns(self):
        currentRun = 1
        maxRun = 1
        multiplier = 1
        for num in range(self.handSize - 1):
            if self.sortedNums[self.handSize - 1] == 14 and self.sortedNums[0] == 2:
                currentRun += 1
                continue
            elif self.sortedNums[num + 1] == self.sortedNums[num]:
                multiplier *= 2
                continue
            elif self.sortedNums[num + 1] == self.sortedNums[num] + 1 and self.sortedNums[num + 1] != 14:
                currentRun += 1
                continue
            elif currentRun > maxRun:
                maxRun = currentRun
            currentRun = 1
            multiplier = 1
        if currentRun > maxRun:
            maxRun = currentRun
        if maxRun > 2:
            self.score += maxRun * multiplier

    def checkFifteenTwos(self, numbers, target, partial=[]):
        s = sum(partial)
        # check if the partial sum is equals to target
        if s == target:
            self.score += 2
        if s >= target:
            return  # if we reach the number why bother to continue

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i + 1:]
            self.checkFifteenTwos(remaining, target, partial + [n])

    def scoreHand(self):
        self.sortNums()
        self.reduceFaceValue()
        self.checkPairs()
        self.checkFlush()
        self.checkRuns()
        self.checkFifteenTwos(self.sortedNumsReducedFaceValue, 15)


def main():
    '''cards = [Card(14, 4), Card(9, 3), Card(3, 1), Card(6, 1), Card(5, 4)]
    test = Hand(len(cards))
    test.sendHand(cards)
    test.viewHand()
    test.scoreHand()
    print("Score: ", test.score)'''
    count = 0
    total = 10000
    scores = np.zeros(29)
    while count < total:
        hand = Hand(5)
        hand.generateHand()
        hand.scoreHand()
        scores[hand.score] += 1
        count += 1
    print(scores)

    plt.plot(scores/total)
    plt.title("Score of Cribbage Hands")
    plt.show()


main()
