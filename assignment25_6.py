import pandas as pd

def main() :
    df = pd.DataFrame({'grade' : ['A+', 'B', 'A','C','B+']})
    df['grade'] = df['grade'].map({'A+' : 'excellent', 'A': 'very good', 'B+' : 'good', 'B' : 'avrage', 'C' : 'poor'})

    print(df)
if __name__ == "__main__" :
    main()