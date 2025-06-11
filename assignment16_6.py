def main() :
    obj1 = open("source.txt", "r")
    data = obj1.read()

    obj2 = open("destation.txt", "w")
    
    obj2.write(data)

if __name__ == "__main__" :
    main()