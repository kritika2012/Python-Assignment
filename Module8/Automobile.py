class automobile:
    def __init__(self, make, model, mileage, price):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price

    def set_make(self, x):
        self.make = x

    def set_model(self, x):
        self.model = x

    def set_mileage(self, x):
        self.mileage = x

    def set_price(self, x):
        self.price = x

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_mileage(self):
        return self.get_mileage

    def get_price(self):
        return self.price