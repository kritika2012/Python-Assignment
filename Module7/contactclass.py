class contactclass:
    def __init__(self, name="", phonenumber=0, email=""):
        self.__name = name
        self.__phonenumber = phonenumber
        self.__email = email

    def set_name(self, x):
        self.__name = x

    def set_phonenumber(self, x):
        self.__phonenumber = x

    def set_email(self, x):
        self.__email = x

    def get_name(self):
        return self.__name

    def get_phonenumber(self):
        return self.__phonenumber

    def get_email(self):
        return self.__email

    def __str__(self):
        return ("{}, {}, {}".format(self.__name, self.__phonenumber, self.__email))

def add_details():
    details1 = contactclass()
    name = input("enter your name: ")
    details1.set_name(name)
    email = input("enter your email: ")
    details1.set_email(email)
    phonenumber = int(input("enter your phonenumber: "))
    details1.set_phonenumber(phonenumber)
    return str(details1)

def main():
    file_details = open('details.txt','a+')
    file_details.write(add_details())
    file_details.close()
main()