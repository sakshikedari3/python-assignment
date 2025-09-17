###################################################################################################
# Required Libraries
###################################################################################################s
import pandas as pd
import numpy as np
import seaborn as sns
from seaborn import countplot
from matplotlib.pyplot import figure, show, title
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
import joblib

###################################################################################################
# File Path and Model Path
###################################################################################################s

line = "*" * 44
datapath = "MarvellousTitanicDataset.csv"
model_path = "MarvellousTitanicDataset.joblib"

###################################################################################################
# Function name = read_csv
# description = This function reads a CSV file and returns a DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def ReadCSV(DATAPATH):
    return pd.read_csv(DATAPATH)

###################################################################################################
# Function name = DisplayHead
# description = This function displays the first few records of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def DisplayHead(df):
    print(df.head())
    
###################################################################################################
# Function name = DisplayStatisticalInfo
# description = This function displays the statistical information of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def DisplayStatisticalInfo(df):
    print("statistical information are : ")
    print(line)
    print(df.describe()) # use for prepare and manipulate
    print(line)
    
###################################################################################################
# Function name = DisplayHead
# description = This function displays the first few records of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def DisplayDimension(df):
    print("dimention of dataset is :",df.shape)
    
###################################################################################################
# Function name = 
# description = This function displays the first few records of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def PreprocessData(df):
    df.drop(columns = ['Passengerid','zero'], inplace = True)
    return df

###################################################################################################
# Function name = DisplayHead
# description = This function displays the first few records of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def AnalyzeAndModel(df):
    print("dimention of dataset is :",df.shape)

###################################################################################################
# Function name = DisplayHead
# description = This function displays the first few records of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def Encoding(df):
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace = True)
    return df

###################################################################################################
# Function name = DisplayHead
# description = This function displays the first few records of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def DisplayCountPlot(df):
    figure()
    target = "Survived"
    countplot(data = df, x = target).set_title("survived vs non survive")
    #show()

    figure()
    target = "Survived"
    countplot(data = df, x = target, hue = 'Sex').set_title("based on gender")
    #show()

    figure()
    target = "Survived"
    countplot(data = df, x = target, hue = 'Pclass').set_title("based on pclass")
    #show()

    figure()
    df['Age'].plot.hist().set_title("age report")
    #show()

    figure()
    df['Fare'].plot.hist().set_title("fare report")
    #show()

###################################################################################################
# Function name = DisplayHead
# description = This function displays the first few records of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def DisplayHeatMap(df):
    figure(figsize=(10,6))

    sns.heatmap(df.corr(), annot=True, cmap = "coolwarm")

    title("feature correlation heatmap")
    #show()

###################################################################################################
# Function name = alter
# description = This function alters the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def ModelBuilding(df):
    x = df.drop(columns = ['Survived'])
    y = df['Survived']
    return x, y

###################################################################################################
# Function name = DisplayHead
# description = This function displays the first few records of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def display_dimention(x, y):
    print("dimentation of target : ",x.shape)
    print("dimentation of label : ",y.shape)

###################################################################################################
# Function name = scaler
# description = This function scales the features using StandardScaler.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def scaler(x) :
    scaller = StandardScaler()
    x_scale = scaller.fit_transform(x)
    return x_scale

###################################################################################################
# Function name = printSize
# description = This function prints the size of the independent and dependent variables.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def PrintSize(x, y):
    print("independent variables are : Head Size")
    print("dependent variables are : Brain Weight")
    print("total records in data set :", x.shape)
    print("total records in data set :",len(x))
    print("total records in data set :", y.shape)
    print("total records in data set :",len(y))

###################################################################################################
# Function name = printSize
# description = This function prints the size of the independent and dependent variables.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def TrainTestSplit(x_scale, y) :
    a, b, c, d = train_test_split(x_scale, y, test_size=0.2, random_state=42)
    return a, b, c, d

###################################################################################################
# Function name = PrintTrainingTestSize
# description = This function prints the size of the training and testing datasets.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def PrintTrainingTestSize(x_train, x_test, y_train, y_test):
    print("dimentions of traing data set :",len(x_train))
    print("dimentions of traing data set :",len(x_test))
    print("dimentions of traing data set :",len(y_train))
    print("dimentions of traing data set :",len(y_test))
    
###################################################################################################
# Function name = DisplayHead
# description = This function displays the first few records of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def FitModel(x_train, y_train) :

    model = LogisticRegression()

    model.fit(x_train, y_train)
    
    return model

###################################################################################################
# Function name = save_model
# description = This function saves the trained model using joblib.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def save_model(model, model_path):
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
    
###################################################################################################
# Function name = load_model
# description = This function loads the trained model using joblib.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def load_model(model_path):
    print(f"Loading model from {model_path}")
    return joblib.load(model_path)


###################################################################################################
# Function name = DisplayHead
# description = This function displays the first few records of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def Accuracy(y_test, y_pred) :
    return accuracy_score(y_test, y_pred)
    
###################################################################################################
# Function name = DisplayHead
# description = This function displays the first few records of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def ConfusionMatrics(y_test, y_pred) :
    return confusion_matrix(y_test, y_pred)

###################################################################################################
# Function name = Main
# description = this function from where execution start
# description = This function preprocesses the dataset and trains the model and calls the given functions.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def main() :
    
    #1)Load csv file
    df = ReadCSV(datapath)
    print("dataset loaded succesfully")
    
    #2)display head
    DisplayHead(df)
    
    #3)display statistical information
    DisplayStatisticalInfo(df)
    
    #4)Display dimensions
    DisplayDimension(df)
    
    #5)
    df = PreprocessData(df)
    
    AnalyzeAndModel(df)
    
    Encoded_df = Encoding(df)
    
    DisplayCountPlot(Encoded_df)
    
    DisplayHeatMap(Encoded_df)
    
    x, y = ModelBuilding(Encoded_df)
    
    display_dimention(x, y)
    
    x_scale = scaler(x)
    
    PrintSize(x, y)
    
    x_train, x_test, y_train, y_test = TrainTestSplit(x_scale, y)
    
    PrintTrainingTestSize(x_train, x_test, y_train, y_test)
    
    model = FitModel(x_train, y_train)
    
    y_pred = model.predict(x_test)
    
    save_model(model, model_path)
    
    load_model(model_path)
    
    accuracy = Accuracy(y_test, y_pred)
    print("accuracy is ::",accuracy)

    cm = ConfusionMatrics(y_test, y_pred)
    print("confusion matrics is :")
    print(cm)

###################################################################################################
# application starter
###################################################################################################
if __name__ == "__main__" :
    main()
