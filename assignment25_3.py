import pandas as pd

def main() :
    data = {'city' : ['pune','mumbai','delhi','pune','mumbai']}

    df = pd.DataFrame(data)

    df['city'] = df['city'].map({'pune' : 0, 'mumbai' : 1, 'delhi' : 2})

    print(df)


if __name__ == "__main__" :
    main()
