import Deck_player as dp
nm=input('players enter Your name ')
obj=dp.Player(nm)

while(obj.play()):
    obj.show_hand()
    pass
    

