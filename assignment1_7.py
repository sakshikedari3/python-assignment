def chkNum(no) :
    if no % 5 == 0:
        print(True)
    else :
        print(False)

def main():
    print("Enter the number : ")
    num = int(input())
    chkNum(num)

if __name__ == "__main__" :
    main()