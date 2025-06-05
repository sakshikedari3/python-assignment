class books :
    def __init__(self, a, b):
        self.name = a
        self.__price = b

    def display(self) :
        print("inside display function")
        print(self.name)
        print(self.__price)

    def get_price(self) :
        return self.__price

def main () :
    name = input("enter name of books : ")
    price = int(input("enter the price of book : "))

    obj = books(name, price)
    obj.display()

    print("inside main function")

    print(obj.name)
    print(obj.get_price())

if __name__ == "__main__" :
    main()

    