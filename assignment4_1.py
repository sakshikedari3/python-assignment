import sys

sqt = lambda a : a ** 2

def main():
    if len(sys.argv) > 2 :
        print("Error while accepting inputs")
        print("Press --h for help or --u for usage")
        return
    
    if len(sys.argv) == 2 :

        if sys.argv[1] == "--h" :
            print("this program is use to get power of 2 for given number")
            return

        if sys.argv[1] == "--u" :
            print("You can enter number on command line directly or at the time of executing code")
            return
    
        no = int(sys.argv[1])

    else :
        no = int(input("Enter the number : "))

    result = sqt(no)

    print("result is : ",result)

if __name__ == "__main__" :
    main()