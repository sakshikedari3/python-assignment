def chkNum(no) :
    if  no < 0 :
        print("Negative number")
    elif no == 0 :
        print("zero")
    else :
        print("Positive number")
    
def main():
    print("Enter the number : ")
    num =  int(input())
    chkNum(num)
    
if __name__ == "__main__" :
    main()