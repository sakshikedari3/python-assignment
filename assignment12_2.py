class circle :
    pi = 3.14
    def __init__ (self, a) :
        self.radius = a

    def calculateArea(self) :
        area = circle.pi * self.radius * self.radius
        return area
    
    def calculateCircumference(self) :
        circumference = 2 * (circle.pi * self.radius)
        return circumference
    
def main() :
    radius = float(input("enter the radius of circle : "))
    obj = circle(radius) 

    Area = obj.calculateArea()
    Circumference = obj.calculateCircumference()

    print("Radius of circle is :",radius,"\narea of circle is :",Area,"\ncircumference of circle is :",Circumference)

if __name__ == "__main__" :
    main()
