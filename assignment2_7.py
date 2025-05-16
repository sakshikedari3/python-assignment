#print 1 to no in enter number pattern
import sys

def pattern(value) :
    for n in range(1, value + 1) :
        for a in range(1, value + 1) :
            print(a , end = "")
        print()

def main():
    if len(sys.argv) > 2 :
        print("Error while accepting inputs")
        print("Press --h for help or --u for usage")
        return
    
    if len(sys.argv) > 2 :
        
        if sys.argv[1] == "--h" :
            print("this program is use to get pattern")
            return

        if sys.argv[1] == "--u" :
            print("You can enter number on command line directly or at the time of executing code")
            return
    
        no = int(sys.argv[1])

    else :
        no = int(input("Enter the number : "))

    pattern(no)


if __name__ == "__main__" :
    main()