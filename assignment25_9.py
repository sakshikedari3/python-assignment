import pandas as pd

def main() :
    data = {'marks' : [45, 67, 88, 32, 76]}

    df = pd.DataFrame(data)

    df['marks'] = df['marks'].apply(lambda x : 'fail' if x < 50 else x)

    print(df)
    
if __name__ == "__main__" :
    main()