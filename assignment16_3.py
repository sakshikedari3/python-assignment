def main() :
    obj = open("hello.txt", "r")

    data = obj.read()

    line = 0
    word = 0
    character = 0

    for n in data :
        character += 1

        if n == "\n" :
            line += 1

        if n == " ":
            word += 1

    print("lines in file are :",line)
    print("words in file are :",word)
    print("character in file are :",character)


if __name__ == "__main__" :

    main()