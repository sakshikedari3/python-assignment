import pandas as pd

def main() :

    data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}

    df = pd.DataFrame(data)

    data = pd.get_dummies(df, columns=['Department'], prefix = 'Department', dtype = int)

    print(data)

if __name__ == "__main__" :
    main()