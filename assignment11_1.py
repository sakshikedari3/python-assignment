"""def numbers(no) :
    n = 0
    while n <= no :
        print(n)
        n = n + 1"""
n = 0

def numbers(no) :
    global n
    while n <= no:
        print(n)
        n = n + 1
        numbers(no)

def main() :
    no = int(input("enter the number : "))
    numbers(no)

if __name__ == "__main__" :
    main()