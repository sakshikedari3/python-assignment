class base :
    def __init__ (self, a, b) :
        self.name = a
        self.age = b

    def displays (self) :
        print("name of student is :",self.name)
        print("age of student is :",self.age)

class teacher(base) :
    def __init__ (self, a, b) :

        super().__init__(a,b)

    def displayt(self) :
        print("subject is :english")
        print("salary :34000")

def main():
    name = input("enter the name  : ")
    age = int(input("enter your age : "))
    obj = teacher(name, age)

    obj.displays()

    obj.displayt()

if __name__ == "__main__" :
    main()



        