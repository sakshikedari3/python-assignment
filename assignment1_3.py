def addition(value1, value2) :
    ans = value1 + value2
    return ans

def main() :
    print("enter first number : ")
    no1 = int(input())

    print("enter second number : ")
    no2 = int(input())
    
    result = addition(no1, no2)

    print("addition of two numbers is : ",result)

if __name__ == "__main__" :
    main()