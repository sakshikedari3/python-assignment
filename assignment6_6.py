#pattern
import sys

def pattern(value) :
    for n in range(1, value + 1):
        for i in range(n) :
            print("*", end = "")
        print()

def main():
    if len(sys.argv) == 2 :
        no = int(sys.argv[1])

    else :
        no = int(input("Enter the number : "))
    
    pattern(no)

if __name__ == "__main__" :
    main()