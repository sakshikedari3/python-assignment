class rectangle :
    def __init__(self, a, b):
        self.width = a
        self.height = b

    def area(self) :
        ret = self.width * self.height
        print("area of rectangle is :",ret)

    def perimeter(self) :
        ret = 2 * (self.width + self.height)
        print("area of rectangle is :",ret)

def main() :
    width = int(input("enter width : "))
    height = int(input("enter height : "))

    obj = rectangle(width, height)

    obj.area()
    obj.perimeter()

if __name__ == "__main__" :
    main()