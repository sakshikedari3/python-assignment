#arithmatic modul 
from assignment_arithmatic import add, sub, multiply, div
import sys

def main():
    if len(sys.argv) > 4 :
          print("Error while accepting inputs")
          print("Press --h for help or --u for usage")
          return
    if len(sys.argv) > 1 :
        if sys.argv[1] == "--h" :
              print("this program is use to do opreation like addition, subtraction, multiplaction, division")
              return

        if sys.argv[1] == "--u" :
              print("You can select the options like 'add , +', 'sub , -', 'multiply , *', 'div , /' and type it on command line directly or at the time of executing code")
              print("And after that you need to enter 2 number on which you have to perform operations ")
              return
      
        a = sys.argv[1]
        no1 = int(sys.argv[2])
        no2 = int(sys.argv[3])

    else :
        print("Choose \n1. Add or +\n2. Sub or -\n3. Multiply or *\n4. Div or /")
        print("Enter the opreation you want to perform : ")
        a = input()

        no1 = int(input("Enter the first number : "))
        no2 = int(input("Enter the first number : "))
        

    if a == "add" or a == "+" :
            result = add(no1, no2)
            
    elif a == "sub" or a == "-" :
            result = sub(no1, no2)
        
    elif a == "multiply" or a == "*":
            result = multiply(no1, no2)
        
    elif a == "div" or a == "/":
            result = div(no1, no2)
    
    else :
          print("invalid optation seleted !!!")
        
    print("result is : ",result)

if __name__ == "__main__" :
    main()