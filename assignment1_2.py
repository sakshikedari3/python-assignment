def chkNum(no) :
    if no % 2 == 0 :
        print("Even Number")
    else :
        print("Odd Number")
    return 

def main() :
    print("Enter number : ")
    no = int(input())
    chkNum(no)

if __name__ == "__main__" :
    main()