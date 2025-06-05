class bankaccount :
    def __init__(self, a, b, c, d, e):
        self.account_number = a
        self.name = b
        self.balance = c
        self.balanced = d
        self.balancew = e

    def deposite(self) :
        return self.balanced + self.balance
    
    def withdrawl(self) :
        return self.balance - self.balancew
    
def main() :
    name = input("enter your name : ")
    account_number = int(input("enter your id : "))
    balance = int(input("enter your balance : "))
    depositea = int(input("enter the amount you wnat to deposite : "))
    withdrawla = int(input("enter the amount you wnat to withdrawl : "))

    obj = bankaccount(account_number, name, balance, depositea, withdrawla)

    print("name :",name,", account number :",account_number,", balance :",balance)

    print("amount when deposited :",obj.deposite())
    print("amount when withdrawl :",obj.withdrawl())

if __name__ == "__main__" :
    main()
    