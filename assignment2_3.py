# factorial
import sys

def factorical(value) :
    a = 1
    for n in range(value, 1, -1) :
        a = a * n
    return a

def main():
    if len(sys.argv) > 2 :
          print("Error while accepting inputs")
          print("Press --h for help or --u for usage")
          return
    if len(sys.argv) == 2 :
        if sys.argv[1] == "--h" :
              print("this program is use to factriol of given number")
              return

        if sys.argv[1] == "--u" :
              print("You can enter number on command line directly or at the time of executing code to get output")
              return
        
        no = int(sys.argv[1])

    else :
        no = int(input("enter the number : "))

    result = factorical(no)

    print("Factriol of number is : ",result)
    
if __name__ == "__main__" :
    main()