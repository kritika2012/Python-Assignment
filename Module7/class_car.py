class car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return f'A {self.color} car'

def main():
    obj=car("Black",555.5)
    print(obj)
main()
