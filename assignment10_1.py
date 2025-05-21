def main ():
    no = int(input("enter the number : "))

    print("result is :",(lambda x : x ** 2)(no))

if __name__ == "__main__" :
    main()