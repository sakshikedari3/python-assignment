#vote
import sys

def chk(value) :
    if value > 18 :
        print("Eligible to vote")

    else :
        print("Not eligible for voteing")

def main():
    if len(sys.argv) == 2 :
        age = int(sys.argv[1])

    else :
        age = int(input("Enter your age : "))

    chk(age)

if __name__ == "__main__" :
    main()