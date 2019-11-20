## Author: Stephen Scott
## Date: November 19, 2019


import random

class Card:
	def __init__(self):
		self.num = random.randint(1,10)
		self.suit = random.randint(1,4)

class Hand:
	def __init__(self, handsize):
		self.handsize = handsize
		self.cards = []
	def getHandSize(self):
		print(self.handsize)
	def createHand(self):
		for i in range(self.handsize):
			self.cards.append(Card())
	def viewHand(self):
		for i in range(self.handsize):
			print ("Num: ", self.cards[i].num, "\tSuit: ", self.cards[i].suit)


#class Score:
	#def __init__(self, hand, score):
	#	self.hand = hand
	#	self.score = score
	#def fifteenTwo(self):
		#some code
	#def run(self):
		#some code
	#def suited(self):
		#some code


def main():
	newHand = Hand(6)
	newHand.getHandSize()
	newHand.createHand()
	newHand.viewHand()
	#Score()

main()