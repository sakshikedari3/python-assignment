"""def sum(no) :
    a = 1
    b = 0
    while a <= no :
        b = b + a
        print(b)
        a = a + 1
    return b"""
a = 1
b = 0
def sum(no) :
    global a, b
    while a <= no :
        b = b + a
        a = a + 1
        sum(no)
    return b


def main () :
    no = int(input("enter the number : "))

    ret = sum(no)

    print("result is :",ret)

if __name__ == "__main__" :
    main()