
#if player has score of cards greater than 20 he/she  wins else looses 
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

#main function
def main():
    winscore = 20
    plycount = 0
    count=0
    pllst = []
    dec1 = Deck()
    dec1.shuffle_deck()
    plycount = 0
    while True:
        plycount += game(pllst,dec1)
        if(plycount>20):
            print("you won")
            break
        elif(plycount<20 and count==10):
            print("you loose")
            break
        elif(plycount==20):
            print("tie")
            break
        count+=1
main()
