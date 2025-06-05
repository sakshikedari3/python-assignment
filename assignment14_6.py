class calculator :
    def __init__(self, a, b):
        self.no1 = a
        self.no2 = b

    def addition(self) :
        return self.no1 + self.no2
    
    def subtraction(self) :
        return self.no1 - self.no2
    
    def multiplaction(self) :
        return self.no1 * self.no2
    
    def division(self) :
        return self.no1 / self.no2
    
def main() :
    no1 = int(input("enter first value : "))
    no2 = int(input("enter second value : "))

    obj = calculator(no1, no2)

    print("addition of numbers is :",obj.addition())
    print("subtraction of numbers is :",obj.subtraction())
    print("multiplaction of numbers is :",obj.multiplaction())
    print("division of numbers is :",obj.division())

if __name__ == "__main__" :
    main()