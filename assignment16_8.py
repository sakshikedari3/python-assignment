def main():
    obj = open("source.txt", "r")
    data = obj.readlines()

    obj.close()

    obj1 = open("text.txt", "w")

    for line in data :
        if len(line) > 2 :
            obj1.write(line) 

if __name__ == "__main__" :
    main()
            