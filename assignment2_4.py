#addition of factor
import sys

def factor(value) :
    i = 0
    for n in range(1, value + 1) :
        if value % n == 0 :
            print(n)
            i += n
    return i   

def main():
    if len(sys.argv) > 2 :
          print("Error while accepting inputs")
          print("Press --h for help or --u for usage")
          return
    
    if len(sys.argv) > 1 :
    
        if sys.argv[1] == "--h" :
                print("this program is use to get addition of factors of entered number")
                return

        if sys.argv[1] == "--u" :
                print("You can enter number on command line directly or at the time of executing code")
                return
        
        no = int(sys.argv[1])

    else :
          
        no = int(input("enter the number : "))

    result = factor(no)

    print("Addition of factors is : ",result)

if __name__ == "__main__" :
    main()