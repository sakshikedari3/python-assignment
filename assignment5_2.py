#vowels
import sys

def vowel(value) :
    b = ["A","E","I","O","U","a","e","i","o","u"]
    return value in b

def main():
    if len(sys.argv) == 2 :
        word = sys.argv[1]

    else :
        word = input("Enter the character : ")

    result = vowel(word)

    if result :
        print("'",word,"' charater is vowel")

    else :
        print("'",word,"' charater is not vowel")

if __name__ == "__main__" :
    main()