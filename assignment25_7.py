import pandas as pd

def main() :
    data = {'age' : [18, 22, 25, 30, 35]}
    ans = []

    df = pd.DataFrame(data)

    maximim = df['age'].max()
    minimum = df['age'].min()

    for i in df['age'] :
        a = (i - minimum) / (maximim - minimum)
        a = round(float(a), 2)
        ans.append(a)

    print("normalized values are :",ans)

if  __name__ == "__main__" :
    main()