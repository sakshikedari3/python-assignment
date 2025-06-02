class demo :
    value = 12
    def __init__ (self, a, b) :
        self.no1 = a
        self.no2 = b

    def fun(self) :
        print("fun :",self.no1)

    def gun(self) :
        print("gun :",self.no2)

def main() :
    obj1 = demo(11,21)
    obj2 = demo(51,101)

    obj1.fun()
    obj1.gun()
    obj2.fun()
    obj2.gun()

if __name__ == "__main__" :
    main()