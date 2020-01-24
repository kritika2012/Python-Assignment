import random
class Coin:
    def __init__(self):
        self.sideup='heads'
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup='heads'
        else:
            self.sideup='tails'

    def get_side(self):
        return self.sideup


def main():
    cn=Coin()
    print("side",cn.get_side())
    print("I am tossing the coin")
    cn.toss()
    print("new occured side is ",cn.get_side())


main()
