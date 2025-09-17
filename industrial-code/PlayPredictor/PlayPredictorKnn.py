###################################################################################################
# Required Libraries
###################################################################################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier
import joblib

###################################################################################################
# File path
###################################################################################################
line = "-" * 42
dataset = "PlayPredictor.csv"
model_path = "breast_cancer_model.joblib"

###################################################################################################
# Function name = ReadCsv
# description = This function reads a CSV file and returns a DataFrame.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def ReadCsv(datapath) :
    return pd.read_csv(datapath)
    
###################################################################################################
# Function name = display_head
# description = This function displays the head of a DataFrame.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def display_head(datapath) :
    print(datapath.head())
    print(line)
    
###################################################################################################
# Function name = Describe
# description = This function displays the description of a DataFrame.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def Describe(df) :
    print(df.describe())
    print(line)
    
###################################################################################################
# Function name = DisplayInfo
# description = This function displays the information of a DataFrame.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def DisplayInfo(df) :
    print(df.info())
    print(line)
    
###################################################################################################
# Function name = DisplayColumns
# description = This function displays the columns of a DataFrame.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def DisplayColumns(df) :
    print(df.columns)
    print(line)
    
###################################################################################################
# Function name = DisplayDatatypes
# description = This function displays the datatypes of a DataFrame.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def DisplayDatatypes(df) :
    print(df.dtypes)
    print(line)
    
###################################################################################################
# Function name = HeatMap
# description = This function displays the heatmap of correlations in a DataFrame.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def HeatMap(df) :
    plt.figure(figsize = (10, 6))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm', fmt = '.2f')
    plt.title('Correlation Heatmap')
    plt.show()
        
###################################################################################################
# Function name = Encoding
# description = This function encodes categorical variables into numerical format.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def Encoding(df):
    df['Whether'] = df['Whether'].map({'Sunny' : 0, 'Overcast' : 1, 'Rainy' : 2})
    df['Temperature'] = df['Temperature'].map({'Hot' : 0, 'Mild' : 1, 'Cool' : 2})
    df['Play'] = df['Play'].map({'Yes' : 1, 'No' : 0})
    return df

###################################################################################################
# Function name = alter
# description = This function alters the DataFrame for model training.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def alter(df) :
    x = df.drop(columns=['Play'])
    y = df['Play'] 
    return x, y

###################################################################################################
# Function name = model_training
# description = This function splits the data into training and testing sets.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def model_training(x, y) :
    a, b, c, d = train_test_split(x, y, test_size=0.2, random_state=42) 
    return a, b, c, d

###################################################################################################
# Function name = fit_model
# description = This function fits the KNN model.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def fit_model(x_train, y_train) :

    model = KNeighborsClassifier(n_neighbors=9)
    model.fit(x_train, y_train)
    return model

###################################################################################################
# Function name = SaveModel
# description = This function saves the trained model to a file.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def SaveModel(model, model_path) :
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
    
###################################################################################################
# Function name = LoadModel
# description = This function loads a trained model from a file.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def LoadModel(model_path) :
    model = joblib.load(model_path)
    print(f"Model loaded from {model_path}")
    return model

###################################################################################################
# Function name = accuracy
# description = This function calculates the accuracy of the model.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def accuracy(y_test, y_pred) :
    return accuracy_score(y_test, y_pred)

###################################################################################################
# Function name = confusion
# description = This function calculates the confusion matrix of the model.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def confusion(y_test, y_pred) :
    return confusion_matrix(y_test, y_pred)

###################################################################################################
# Function name = DisplayConfusionMatrix
# description = This function displays the confusion matrix of the model.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def DisplayConfusionMatrix(cm, model) :
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(cmap=plt.cm.Blues)
    plt.show()
    
###################################################################################################
# Function name = classification
# description = This function calculates the classification report of the model.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def classification(y_test, y_pred) :
    print(classification_report(y_test, y_pred))
    
###################################################################################################
# Function name = plot_graph
# description = This function plots the graph of the model's performance.
# author = sakshi kedari
# date = 17-8-2025
###################################################################################################
def plot_graph(x, y) :
    plt.scatter(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot')
    plt.show()

###################################################################################################
# Function name = main
# description = this function from where execution start
# description = This function preprocesses the dataset and trains the model and calls the given functions.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################
def main() :
    #1) Read CSV file
    df = ReadCsv(dataset)
    
    #2) Display head
    display_head(df)
    
    #3) Describe
    Describe(df)
    
    #4) Display Info
    DisplayInfo(df)
    
    #5) Display Columns
    DisplayColumns(df)
    
    #6) Display Datatypes
    DisplayDatatypes(df)
    
    #7) Encoding
    df = Encoding(df)
    
    #8) HeatMap
    HeatMap(df)
    
    #9) Alter
    x, y = alter(df)
    
    #10) Model Training
    x_train, x_test, y_train, y_test = model_training(x, y)
    
    #11) Fit Model
    model = fit_model(x_train, y_train)
    
    #12) Save Model
    SaveModel(model, model_path)
    
    #13) Load Model
    model = LoadModel(model_path)
    
    #14) Prediction
    y_pred = model.predict(x_test)
    
    #15) calculate and print accuracy
    Accuracy = accuracy(y_test, y_pred)
    print("accuracy is :",Accuracy)
    
    #16) confusion matrix
    cm = confusion(y_test, y_pred)
    print("confusion matrix is :\n",cm)
    
    #17) Display confusion matrix
    DisplayConfusionMatrix(cm, model)
    
    #18) classification report
    classification(y_test, y_pred)
    
    #19) plot graph
    plot_graph(x_test.iloc[:, 0], y_test)

###################################################################################################
# application starter
###################################################################################################
if __name__ == "__main__" :
    main()
