def main():
    obj = open("hello.txt", "r")
    ret = obj.read()

    print("data is :",ret)

if __name__ == "__main__" :
    main()