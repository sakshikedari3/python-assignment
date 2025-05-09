def pattern(no) :
    for i in range(no) :
        print("*")

def main():
    print("Enter the number : ")
    num = int(input())
    pattern(num)

if __name__ == "__main__" :
    main()