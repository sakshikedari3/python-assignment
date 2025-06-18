import sys

def check(filename, word) :
    count = 0

    obj = open(filename, "r")
    data = obj.read()

    for n in data :
        if n == word :
            count += 1

    print("frequency of word is : ",count)

def main () :
    if len(sys.argv) == 3 :
        filename = sys.argv[1]
        word = sys.argv[2]

    elif len(sys.argv) == 1:
        filename = input("enter file name : ")
        word = input("enter the word you want to find frequency of : ")

    check(filename, word)

if __name__ == "__main__" :
    main()
    