"""def pattern(no) :
    a = 1
    while a <= no:
        b = 1 
        while b <= a:
            print("*", end="")  
            b = b + 1  
        print()  
        a = a + 1 """
a = 1
b = 1
def pattern(no) :
    global a, b
    while a <= no: 
        while b <= a:
            print("*", end="")  
            b = b + 1  
        print()  
        a = a + 1 
        pattern(no)
        
def main () :
    no = int(input("enter the number : "))

    pattern(no)

if __name__ == "__main__" :
    main()
