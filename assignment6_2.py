#sum of even number from 1-100
def main():
    a = 0
    for i in range(1, 101):
        if i % 2 == 0 :
            a += i
    print(a)

if __name__ == "__main__" :
    main()