def main() :
    obj = open("hello.txt", "r")

    data = obj.readlines()

    for line in data :
        word = line.split()

        if len(word) > 5 :
            print(line)

if __name__ == "__main__" :
    main()