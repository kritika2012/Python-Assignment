#This class car inherits the automobile class from the previous Automobile.py file which we have imported in this child.py file
from automobile import automobile
class car(automobile):
    def __init__(self, make="", model="", mileage=0, price=0, doors=""):
        automobile.__init__(self, make, model, mileage, price)
        self.__doors = doors

    def set_doors(self, x):
        self.__doors = x

    def get_doors(self):
        return self.__doors

class truck(automobile):
    def __init__(self, make="", model="", mileage=0, price=0, drive_type=""):
        automobile.__init__(self, make, model, mileage, price)
        self.__drive_type = drive_type

    def get_drive_type(self, x):
        self.__drive_type = x

    def set_drive_type(self, x):
        return self.__drive_type

class suv(automobile):
    def __init__(self, make="", model="", mileage=0, price=0, pass_cap=""):
        automobile.__init__(self, make, model, mileage, price)
        self.__pass_cap = pass_cap

    def set_pass_cap(x):
        self.__pass_cap = x

    def get_pass_cap(self):
        return self.__pass_cap

def main():
    a_car = car()
    a_truck = truck()
    a_suv = suv()
    a_car.set_make("suzuki")
    a_car.set_model("k100")
    a_car.set_mileage(124)
    a_car.set_price(2151256)
    a_car.set_doors(4)
    print(a_car.get_make(), a_car.get_model(), a_car.get_mileage(), a_car.get_price(), a_car.get_doors())
main()