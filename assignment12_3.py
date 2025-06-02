class arithmatic :
    def __init__ (self, a, b) :
        self.value1 = a
        self.value2 = b

    def addition(self) :
        return self.value1 + self.value2
    
    def subtraction(self) :
        return self.value1 - self.value2
    
    def multiplaction(self) :
        return self.value1 * self.value2
    
    def division(self) :
        return self.value1 / self.value2
    
def main () :
    value1 = int(input("enter the first value : "))
    value2 = int(input("enter the second value : "))

    obj = arithmatic(value1, value2)

    add = obj.addition()
    sub = obj.subtraction()
    multi = obj.multiplaction()
    div = obj.division()

    print("1st number :",value1," 2nd number :",value2,"\naddition :",add,"\nsubtraction :",sub,"\nmultiplaction :",multi,"\ndivision :",div)

if __name__ == "__main__" :
    main()
    
