###################################################################################################
# Required Libraries
###################################################################################################s
import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


###################################################################################################
# File Path and Model Path
###################################################################################################s

line = "*" * 44
datapath = "HeadBrain.csv"
model_path = "HeadBrainLinearModel.joblib"

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
    print(line)
    print("first few records of the data set are : ")
    print(line)
    print(df.head())
    print(line)

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
# Function name = HeatMap
# description = This function displays the heatmap of the correlation matrix of the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
    
def HeatMap(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Heatmap of HeadBrain Dataset")
    plt.show()
    
###################################################################################################
# Function name = alter
# description = This function alters the DataFrame.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def alter(df):
    x = df[['Head Size(cm^3)']]
    y = df[['Brain Weight(grams)']]
    return x, y

###################################################################################################
# Function name = scaler
# description = This function scales the features using StandardScaler.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def scaler(x) :
    return StandardScaler().fit_transform(x)

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
def TrainTestSplitDf(x, y):
    a, b, c, d = train_test_split(x, y, test_size = 0.2, random_state = 42)
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
# Function name = fit
# description = This function fits the linear regression model.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def fit(x_train, y_train):
    model = LinearRegression()
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
# Function name = mean_square_error
# description = This function calculates the mean square error.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def mean_square_error(y_test, y_pred):
    return mean_squared_error(y_test, y_pred)

###################################################################################################
# Function name = root_mean_square_error
# description = This function calculates the root mean square error.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def root_mean_square_error(mse):
    return np.sqrt(mse)

###################################################################################################
# Function name = r2score
# description = This function calculates the R^2 score.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################
def r2score(y_test, y_pred):
    return r2_score(y_test, y_pred)

###################################################################################################
# Function name = ScatterPlot
# description = This function creates a scatter plot of the actual vs predicted values.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################

def scatterPlot(x_test, y_test, y_pred):

    print("visual represention")

    plt.figure(figsize=(8,5))

    plt.scatter(x_test, y_test, color = 'blue', label = 'actual')

    plt.plot(x_test, y_pred, color = 'red', linewidth = 2, label = 'regression line')

    plt.xlabel("Head Size(cm^3)")

    plt.ylabel("Brain Weight(grams)")

    plt.title("head-brain ")

    plt.legend()

    plt.grid(True)

    plt.show()
    
###################################################################################################
# Function name = Main
# description = this function from where execution start
# description = This function preprocesses the dataset and trains the model and calls the given functions.
# author = sakshi kedari
# date = 16-9-2025
###################################################################################################

def main() :
    #1) read csv file
    df = ReadCSV(datapath)
    
    #2) display first few records
    DisplayHead(df)
    
    #3) display statistical information
    DisplayStatisticalInfo(df)
    
    #4) heat map
    HeatMap(df)
    
    #5) alter the dataframe to get independent and dependent variables
    x, y = alter(df)

    #6) scale the independent variables
    x = scaler(x)

    #7) print size of independent and dependent variables
    PrintSize(x, y)

    #8) split the data into training and testing datasets
    x_train, x_test, y_train, y_test = TrainTestSplitDf(x, y)
    
    #9) print size of training and testing datasets
    PrintTrainingTestSize(x_train, x_test, y_train, y_test)

    #10) fit the model
    model = fit(x_train, y_train)

    #11) predict the model
    prediction = model.predict(x_test)

    #12) save the model
    save_model(model, model_path)

    #13) load the model
    model1 = load_model(model_path)

    #14) predict using the loaded model
    prediction = model1.predict(x_test)

    #15) calculate and print the evaluation metrics
    mse = mean_square_error(y_test, prediction)
    print("Mean Square Error:", mse)

    #16) calculate and print the root mean square error
    rmse = root_mean_square_error(mse)
    print("Root Mean Square Error:", rmse)

    #17) calculate and print the R^2 score
    r2 = r2score(y_test, prediction)
    print("R^2 Score:", r2)

    #18) visualize the results using scatter plot
    scatterPlot(x_test, y_test, prediction)
    
###################################################################################################
# application starter
###################################################################################################
if __name__ == "__main__" :
    main()
