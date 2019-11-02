#!/usr/bin/env python3

import random, os, sys

cardName = { 1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King' }
cardSuit = { 'c': 'Clubs', 'h': 'Hearts', 's': 'Spades', 'd': 'Diamonds' }

class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
	def __str__(self):
		return(cardName[self.rank]+" of "+cardSuit[self.suit])
	def getRank(self):
		return(self.rank)
	def getSuit(self):
		return(self.suit)
	def value(self):
		if self.rank > 9:
			return(10)
		else:
			return(self.rank)

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    def identify(self):
        return(name)
    def add(self,add):
        hand.append(add)
    def score(self):
        self.score = sum(hand)

player_1 = Player(input("Enter player 1 name.\n"))
player_2 = Player(input("Enter player 2 name.\n"))
player_3 = Player(input("Enter player 3 name.\n"))
player_4 = Player(input("Enter player 4 name.\n"))
player_5 = Player(input("Enter player 5 name.\n"))
player_6 = Player(input("Enter player 6 name.\n"))

deck = []
suits = [ 'c','h','d','s' ]
for suit in suits:
	for rank in range(1,14):
		deck.append(Card(rank,suit))
player_1.add(5)

'''

def showHand(hand):
	for card in hand:
		print(card)

def showCount(hand):
	print("Count: "+str(handCount(hand)))

def handCount(hand):
	handCount=0
	for card in hand:
		handCount += card.BJValue()
	return(handCount)

def gameEnd(score):
	print("Blackjack! *Final Score* Computer: "+str(score['computer'])+" You: "+str(score['human']))
	sys.exit(0)

deck = []
suits = [ 'c','h','d','s' ]
for suit in suits:
	for rank in range(1,14):
		deck.append(Card(rank,suit))
score = { 'computer': 0, 'human': 0 }
hand = { 'computer': [],'human': [] }

keepPlaying = True
while keepPlaying:
    # Shuffle
    random.shuffle(deck)
	random.shuffle(deck)
	random.shuffle(deck)
	# Deal Cards
	hand['human'].append(deck.pop(0))
	hand['computer'].append(deck.pop(0))
	hand['human'].append(deck.pop(0))
	hand['computer'].append(deck.pop(0))
	playHuman = True
	bustedHuman = False
	while playHuman:
		os.system('clear')
		print("Blackjack! Computer: "+str(score['computer'])+" You: "+str(score['human']))
		print()
		print('Computer Shows: '+ str(hand['computer'][-1]))
		print()
		print('Your Hand:')
		showHand(hand['human'])
		showCount(hand['human'])
		print()
		inputCycle = True
		userInput = ''
		while inputCycle:
			userInput = input("(H)it, (S)tand, or (Q)uit: ").upper()
			if userInput == 'H' or 'S' or 'Q':
				inputCycle = False
		if userInput == 'H':
			hand['human'].append(deck.pop(0))
			if handCount(hand['human']) > 21:
				playHuman = False
				bustedHuman = True
		elif userInput == 'S':
			playHuman = False
		else:
			gameEnd(score)
	playComputer = True
	bustedComputer = False
	while not bustedHuman and playComputer:
		print(handCount(hand['computer']))
		if handCount(hand['computer'])<17:
			hand['computer'].append(deck.pop(0))
		else:
			playComputer = False
		if handCount(hand['computer'])>21:
			playComputer = False
			bustedComputer = True
	if bustedHuman:
		print('Player Busted')
		score['computer'] += 1
	elif bustedComputer:
		print('Computer Busted')
		score['human'] += 1
	elif handCount(hand['human']) > handCount(hand['computer']):
		print('Player Wins')
		score['human'] += 1
	else:
		print('Computer Wins')
		score['computer'] += 1
	print('\nComputer Hand:')
	showHand(hand['computer'])
	showCount(hand['computer'])
	print('\nPlayer Hand:')
	showHand(hand['human'])
	showCount(hand['human'])
	print()
	if input("(Q)uit or enter for next round").upper() == 'Q':
		gameEnd(score)
	deck.extend(hand['computer'])
	deck.extend(hand['human'])
	del hand['computer'][:]
	del hand['human'][:]
'''
