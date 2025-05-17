#lambda func to sqr and cube
import sys

def main():
    if len(sys.argv) == 2 :
        no = int(sys.argv[1])

    else :
        no = int(input("Enter the number : "))

    #print("square of",no, "is", sqr)
    print("square of",no, "is", (lambda no : no * no) (no))
    print("Cube of",no,"is", (lambda no : no * no * no) (no))

if __name__ == "__main__" :
    main()