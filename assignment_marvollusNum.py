def prime(value) :
    b = 0
    for n in value:
        if n < 2:
            continue 
        for i in range(2, n):
            if n % i == 0:
                break 
        else:
            b += n
            print(n)
    return b
