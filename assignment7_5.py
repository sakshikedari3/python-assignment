#palindrome
import sys

def palindrome(word) :
    rword = ""
    for char in word :
        rword = char + rword

    if word == rword :
        print("the word is palindrom")
    else :
        print("Word is not palindrom")

def main():
    if len(sys.argv) == 2 :
        word = sys.argv[1]

    else :
        word = input("Enter the word : ")


    print(word)

    palindrome(word)

if __name__ == "__main__" :
    main()