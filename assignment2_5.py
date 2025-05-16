# prime no
import sys

def prime(value):
      n = 2
      while (n < value) :
            if value % n == 0:
                return False
                
            else :
                return True
                  
def main():
    if len(sys.argv) > 2 :
        print("Error while accepting inputs")
        print("Press --h for help or --u for usage")
        return
    
    if len(sys.argv) == 2 :
    
        if sys.argv[1] == "--h" :
            print("this program is use to wheather the given number is prime or not")
            return

        if sys.argv[1] == "--u" :
            print("You can enter number on command line directly or at the time of executing code")
            return
    
        no = int(sys.argv[1])

    else :
        no = int(input("Enter the number : "))

    result = prime(no)

    if result == True :
        print("Number is prime")

    else :
        print("Number is not prime")

if __name__ == "__main__" :
    main()