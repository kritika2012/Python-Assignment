# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:51:35 2020

@author: pc
"""
import random
from itertools import product
class Deck():
    suit = ('hearts', 'spades', 'diamond', 'clubs')
    ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight',
             'nine', 'ten', 'jack', 'queen', 'king', 'ace')
    values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,
             'eight':8,'nine':9, 'ten':10, 'jack':11,
             'queen':12, 'king':13, 'ace':1,}
    def __init__(self):
        self.deck1 = list(product(Deck.suit,Deck.ranks))
        random.shuffle(self.deck1)
    def draw_card(self):
        if len(self.deck1) == 0:
            return 0
        else:
            return self.deck1.pop()
    def shuffle_deck(self):
        random.shuffle(self.deck1)
        return str(self.deck1)[1:11]


class Card(Deck):
    def __init__(self,deck):
        self.card = deck.draw_card()
        if self.card == 0:
            print("Deck is now empty")
        self.suit = self.card[0]
        self.rank = self.card[1]
        self.value = self.values[self.rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    def getval(self):
        return self.value

def game(lst,deck):
    lst.append(Card(deck))
    return lst[-1].value
#winscore here is the score which is to be reached by the sum of cards when picked up by computer and player
winscore = 20
plycount,comcount = 0,0

#main function
def main():
    count=0
    pllst = []
    cmplst = []
    dec1 = Deck()
    dec2 = Deck()
    dec1.shuffle_deck()
    dec2.shuffle_deck()
    plycount, comcount = 0, 0
    while True:
        plycount += game(pllst,dec1)
        comcount += game(pllst, dec2)
        if ((plycount == winscore) or (plycount>winscore and plycount!=comcount)):
            print(f'You Won, computer number was {comcount} player number was {plycount}')
            break
        if (comcount == winscore or (comcount>winscore and plycount!=comcount)):
            print(f'You Lost, computer number was {comcount} player number was {plycount}')
            break
        elif(count==10):
            print('it is a tie game')
        count+=1

main()