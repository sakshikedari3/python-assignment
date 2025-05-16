import sys

multiply = lambda no1, no2 : no1 * no2

def main():
    if len(sys.argv) > 3 :
        print("Error while accepting inputs")
        print("Press --h for help or --u for usage")
        return
    
    if len(sys.argv) == 3 :

        if sys.argv[1] == "--h" :
            print("this program is use to factriol of given number")
            return

        if sys.argv[1] == "--u" :
            print("You can enter number on command line directly or at the time of executing code")
            return
        
        no1 = int(sys.argv[1])
        no2 = int(sys.argv[2])

    else :
        no1 = int(input("Enter the first number : "))
        no2 = int(input("Enter the second number : "))

    result = multiply(no1, no2)

    print("Result is : ",result)    

if __name__ == "__main__" :
    main()