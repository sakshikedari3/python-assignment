def main ():
    no1 = int(input("enter the number : "))
    no2 = int(input("enter the number : "))

    print("result is :",(lambda x, y : x * y)(no1, no2))

if __name__ == "__main__" :
    main()