"""def factroial(no) :
    i = 1
    a = 1
    while i <= no :
        a = a * i
        i = i + 1
    return a"""
a = 1
i = 1
def factroial(no) :
    global a, i
    while i <= no :
        a = a * i
        i = i + 1
        factroial(no)
    return a

def main () :
    no = int(input("enter the number : "))
    ret = factroial(no)

    print("result is :",ret)

if __name__ == "__main__" :
    main()
