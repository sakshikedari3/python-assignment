###################################################################################################
# Required Libraries
###################################################################################################
import pandas as pd
import seaborn as sns
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import (
    StandardScaler, 
    LabelEncoder)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    roc_auc_score,
    accuracy_score,
    confusion_matrix, 
    ConfusionMatrixDisplay, 
    classification_report,
    roc_curve)

###################################################################################################
# File path
###################################################################################################

line = "-" * 42
dataset = "breast-cancer-wisconsin.csv"
model_path = "breast_cancer_model.joblib"

###################################################################################################
# Dataset Headers
###################################################################################################
headers = ['CodeNumber','ClumpThickness','UniformityCellSize','UniformityCellShape','MarginalAdhesion','SingleEpithelialCellSize','BareNuclei','BlandChromatin','NormalNucleoli','Mitoses','CancerType']

###################################################################################################
# Function name = read_csv
# description = This function reads a CSV file and returns a DataFrame.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def read_csv(datapath) :
    return pd.read_csv(datapath)

###################################################################################################
# Function name = describe
# description = This function print the description of the dataset.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def describe(datapath) :
    print(line)
    print(datapath.describe())
    
###################################################################################################
# Function name = columns
# description = This function prints the columns of the dataset.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################
    
def columns(datapath) :
    print(line)
    print(datapath.columns)
    
###################################################################################################
# Function name = datatypes
# description = This function prints the datatypes of the dataset.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################
    
def datatypes(datapath) :
    print(line)
    print(datapath.dtypes)
    
###################################################################################################
# Function name = encoding
# description = This function encodes categorical features in the dataset and returns the modified DataFrame.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################
    
def encoding(datapath) :
        
    for col in datapath.select_dtypes(include='object') :
        datapath[col] = LabelEncoder().fit_transform(datapath[col])
        
    return datapath

###################################################################################################
# Function name = heatmap
# description = This function show heat map of dataset
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################
    
def heatmap(datapath) :
    sns.heatmap(datapath.corr(), annot = True, cmap = "Purples")
    plt.title("heat map for breast cancer")
    #plt.show()
    
###################################################################################################
# Function name = alter
# description = This function alters the dataset by dropping unnecessary columns.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################
    
def alter(datapath) :
    a = datapath.drop(columns=['CodeNumber','CancerType'])
    b = datapath['CancerType']
    return a, b

###################################################################################################
# Function name = scaler
# description = This function scales the features of the dataset.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def scaler(x):
    data = StandardScaler()
    return data.fit_transform(x)

###################################################################################################
# Function name = trainModel
# description = This function splits the dataset into training and testing sets.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def trainModel(x, y, test, random) :
    a, b, c, d = train_test_split(x, y, test_size=test, random_state=random)
    return a, b, c, d

###################################################################################################
# Function name = fit
# description = This function fits a logistic regression model to the training data.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def fit(x_train, y_train) :
    model = RandomForestClassifier(n_estimators=300)
    model.fit(x_train, y_train)
    return model

###################################################################################################
# Function name = save_model
# description = This function saves the trained model to a file.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def save_model(model_fit, path = model_path):
    joblib.dump(model_fit, path)
    print(f"Model saved to {path}")
    
###################################################################################################
# Function name = load_model
# description = This function loads a trained model from a file.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################
    
def load_model(path = model_path):
    model = joblib.load(path)
    print(f"Model loaded from {path}")
    return model

###################################################################################################
# Function name = accuracy
# description = This function calculates the accuracy of the model.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def accuracy(prediction, y_test) :
    return accuracy_score(y_test, prediction)

###################################################################################################
# Function name = classification
# description = This function return the classification report.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def classification(prediction, y_test) :
    return classification_report(prediction, y_test)

###################################################################################################
# Function name = confusion
# description = This function returns the confusion matrix.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def confusion(prediction, y_test) :
    return confusion_matrix(y_test, prediction) 

###################################################################################################
# Function name = matrixDisplay
# description = This function displays the confusion matrix.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def matrixDisplay(matrix, y_test):
    cmdk = ConfusionMatrixDisplay(matrix, display_labels=np.unique(y_test))
    cmdk.plot(cmap='magma')
    plt.title("confusion matrix")
    
    plt.show()
    
###################################################################################################
# Function name = pair_plot
# description = This function displays the pair plot.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################
    
def pair_plot(datapath) :
    df = read_csv(datapath)
    sns.pairplot(df)
    plt.title("Pair Plot")
    plt.show()
    
###################################################################################################
# Function name = feature_importance
# description = This function displays the feature importance.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def feature_importance(model, feature_names) :
    feature_names = list(feature_names)
    importance = np.array(model.feature_importances_).flatten()
    
    print("Number of feature names:", len(feature_names))
    print("Number of importances:", len(model.feature_importances_))

    if len(feature_names) != len(importance):
        raise ValueError("Length of feature_names and feature_importances_ must match.")

    feature_importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': importance
    }).sort_values(by='importance', ascending=True)
    
    plt.figure(figsize=(10, 6))
    plt.barh(feature_importance_df['feature'], feature_importance_df['importance'], color='skyblue')
    plt.title("Feature Importance")
    plt.xlabel("Importance")
    plt.ylabel("Features")
    plt.tight_layout()
    plt.show()
    
###################################################################################################
# Function name = auc_score
# description = This function calculates the AUC score.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def auc_score(y_test, prediction):
    auc = roc_auc_score(y_test, prediction)
    return auc

###################################################################################################
# Function name = roc_graph
# description = This function displays the ROC curve.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def roc_graph(y_test, prediction):
    lr, tlr, _ = roc_curve(prediction, y_test, pos_label=4)

    plt.plot(lr, tlr, color='blue')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve of logistic regression')
    plt.grid()
    plt.show()

###################################################################################################
# Function name = main
# description = this function from where execution start
# description = This function preprocesses the dataset and trains the model and calls the given functions.
# author = sakshi kedari
# date = 13-8-2025
###################################################################################################

def main() :
    
    # 1)read dataset
    df = read_csv(dataset)

    # 2)Store data set to 'CANCER.CSV'
    df.to_csv('cancer.csv')
    
    # 3)Describe the dataset information
    describe(df)
    
    # 4)Display information of column
    columns(df)
    
    # 5)display datatypes of columns
    datatypes(df)

    # 6)encode categorical features
    df = encoding(df)
    
    # 7)Display heatmap of the dataset
    #heatmap(df)
    
    # 8)Alter the dataset by dropping unnecessary columns
    x, y = alter(df)

    # 9)Scale the features
    x_scale = scaler(x)
    
    # 10)Train the model and print its size
    x_train, x_test, y_train, y_test = trainModel(x_scale, y, 0.2, 42)
    
    print('size of x_train :',x_train.shape)
    print('size of x_test :',x_test.shape)
    print('size of y_train :',y_train.shape)
    print('size of y_test :',y_test.shape)
    
    # 11)Fit the model in algorithm
    model_fit = fit(x_train, y_train)

    # 12)save the model
    save_model(model_fit)
    
    # 13) load the model
    model = load_model()

    # 14) make predictions
    prediction = model.predict(x_test)

    # 15) calculate training and testing accuracy and print that accuracy
    
    accuracy_Training = accuracy(y_train, model.predict(x_train))
    print("training accuracy is :",accuracy_Training)
    
    accuracy_testing = accuracy(prediction, y_test)
    print("Testing accuracy is :",accuracy_testing)

    # 16) generate classification report and print report
    classif = classification(prediction, y_test)
    print("classification report is :\n",classif)

    # 17) generate confusion matrix and display that matrix
    con_mat = confusion(prediction, y_test)
    print("confusion matrix is :\n",con_mat)

    # 18) display confusion matrix in visual format
    #matrixDisplay(con_mat, y_test)
    
    # 19) display pair plot
    #pair_plot(dataset)

    # 20) display feature importance
    #feature_importance(model, x.columns)

    # 21) display auc score 
    AUC_score = auc_score(y_test, prediction)
    print(f"AUC Score: {AUC_score:.4f}")

    # 22) display ROC curve
    #roc_graph(y_test, prediction)

###################################################################################################
# application starter
###################################################################################################

if __name__ == "__main__" :
    main()