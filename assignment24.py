import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def display(data) :
    line = "*" * 44
    df = pd.DataFrame(data)

    print(line)
    print("question 1")
    maximum = df['math'].max()
    minimum = df['math'].min()
    print("maximum marks in math is %s \n minimum marks in math is %s"%(maximum,minimum))
    print(line)

    print("question 2")

    df['gender'] = ['male','male','female']
    df['gender'] = df['gender'].map({'male' : 0, 'female' : 1})
    print(df)

    print(line)
    print("question 3")
    avrage = df.groupby('gender')[['math','science','english']].mean()
    print("avrage marks is : ",avrage)

    print(line)
    print("question 4")
    print("visual representation")
    name = 'sagar'
    marks = df[df['name'] == name].drop(columns = 'name').squeeze()
    plt.pie(marks, labels = marks.index, colors = ['red','blue','green'])
    plt.title("sagar marks")
    plt.show()

    print(line)

    print("question 5")
    df['total'] = df['math'] + df['science'] + df['english']
    df['status'] = df['total'].apply(lambda x : "pass" if x >= 250 else "fail") 
    print(df)

    print(line)
    print("question 6")

    print("number of passed students are :",df['status'].value_counts()['pass'])

    print(line)
    print("question 7")
    print("csv creation")
    df.to_csv("assignmnet24.csv", index=False)
    print(line)

    print("question 8")
    print("visual representation")
    plt.hist(df['math'], color = 'blue')
    plt.title("math marks")
    plt.xlabel("math marks")
    plt.ylabel("number of students ")
    plt.show()
    print(line)

    print("question 9")
    df.rename(columns={'math' : 'mathematics'}, inplace=True)
    print(df)

    print(line)

    print("question 10")
    print("visual representation")
    plt.boxplot(df['english'], patch_artist=True)
    plt.title("boxplot for english marks")
    plt.show()

    print(line)


def main() :
    data = {'name' : ['amit', 'sagar','pooja'],
            'math' : [85, 90, 78],
            'science' : [92, 88, 80],
            'english' : [75, 85, 82]}
    
    display(data)

if __name__ == "__main__" :
    main()