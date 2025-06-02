class numbers :
    def __init__(self, a):
        self.no = a

    def chkprime(self) :
        for n in range(2, self.no) :
            if self.no % n == 0:
                return False
            else:
                return True

    def chkPerfect(self) :
        a = 0
        for n in range(1, self.no) :
            if self.no % n == 0:
                a += n
        if a == self.no :
            return True
        else :
            return False
    
    def factor(self) :
        a = []
        for n in range(1, self.no) :
            if self.no % n == 0:
                a.append(n)
        return a

    def sumOfFactor(self) :
        a = 0
        for n in range(1, self.no) :
            if self.no % n == 0:
                a += n
        return a
    
def main () :
    no = int(input("enter the number : "))

    obj = numbers(no)

    retprime = obj.chkprime()

    if retprime :
        print("NUmber is prime")
    else :
        print("number is not prime")

    retper = obj.chkPerfect()

    if retper :
        print("number is perfect")
    else :
        print("number is not perfect")

    retfac = obj.factor()
    print("list of factors are :",retfac)

    retsum = obj.sumOfFactor()
    print("sum of factors is :",retsum)

if __name__ == "__main__" :
    main()
        