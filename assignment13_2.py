class bankAccount :
    ROI = 10.5
    def __init__ (self, a, b, c, d):
        self.name = a
        self.amount = b
        self.amountd = c
        self.amountw = d

    def display(self) :
        print("name :",self.name)
        print("amount :",self.amount)

    def deposite(self) :
        return self.amount + self.amountd
    
    def withdrawl(self) :
        return self.amount - self.amountw
    
    def calculateIntrest(self) :
        rate = bankAccount.ROI / 100
        intrest = self.amount * rate * 1
        return intrest
    
def main () :
    name = input("enter the name : ")
    amount = int(input("enter the amount : "))
    dep = int(input("enter the amount you want to deposite : "))
    wit = int(input("enter the amount you want to withdrawl : "))

    obj = bankAccount(name, amount, dep, wit)

    obj.display()

    retd = obj.deposite()
    print("total amount is :",retd)

    retw = obj.withdrawl()
    print("total amount is :",retw)

    retc = obj.calculateIntrest()
    print("rate of intrest is :",retc)

if __name__ == "__main__" :
    main()

    