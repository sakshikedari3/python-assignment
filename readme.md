### DEPENDENCIES :



###### INSTALL THE FOLLOWING LIBRARIES:



 	pip install pandas, seaborn, joblib, numpy, matplotlib, sklearn



### DATASET INFORMATION :



#####   	SOURCE :



 		- UCI machine learning repository - Breast-Cancer-Case Study





#####     	FEATURES(10) :



    		1) Code Number



    		2) Clump Thickness



    		3) Uniformity Cell Size



    		4) Uniformity Cell Shape



    		5) Marginal Adhesion



 		6) Single Epithelial Cell Size



    		7) Bare Nuclei



    		8) Bland Chromatin



    		9) Normal Nucleoli



    		10) Mitoses





#####  	TARGET :



   		1) Cancer Type :

 			i) 2 = Benign

 			ii) 4 = Malignant





### WORKFLOW :

#####  	DATA PREPARATION :

 		- Convert raw data file into csv with **headers**

 		- Replace **missing** values with **NaN**

&nbsp;		- Ensure numeric type conversion for all feature columns with **Label Encoder**
		- Convert all type into **integer** using **Standard Scaler**



#####  	TRAIN TEST SPLIT :

 		- Split data into 80% for **Training** and 20% and **Testing**



#####  	MODEL TRAINING AND EVALUATION :

 		- **Metrics** : Accuracy, Classification Report, Confusion Matrices

 		- **Feature Importance Plot** : Show feature importance wise



##### &nbsp;	MODEL SAVING AND LOADING :

&nbsp;		- Save model with  **JOBLIB**

		- Load model for further predictions without retraining



### RUNNING THE PROJECT :

##### &nbsp;	Prepare CSV (Only one) :

&nbsp;		- From breast\_cancer\_pipeline import data\_file\_to\_csv

&nbsp;		- data\_file\_to\_csv()



##### &nbsp;	Train and evalute model :

###### &nbsp;		Expected Output :

&nbsp;			*Training accuracy* : **1.0**



&nbsp;			*Testing accuracy* : **0.9785714285714285**



			*Classification report* : 

&nbsp;				**precision    recall  f1-score   support**



			           **2       0.97      1.00      0.98        86**

			           **4       1.00      0.94      0.97        54**

    			    **accuracy                           0.98       140**

			   **macro avg       0.98      0.97      0.98       140**

			**weighted avg       0.98      0.98      0.98       140**



			*Confusion Matrix :*

				<b>\[\[86  3]</b>

<b> 				\[ 0 51]]</b>



			*Model saved to :* <b>breast\_cancer\_model.joblib</b>





### VISUALIZATIONS :

&nbsp;	- **Heat map** with seaborn

&nbsp;	- **Display Confusion Matrix** with matplotlib

&nbsp;	- **Pair Plot** with seaborn

&nbsp;	- **Feature Importance(Random Forest)**

&nbsp;	- **Roc Curve** with matplotlib



### MODEL STORAGE :

&nbsp;	- Model is saved in **breast\_cancer\_model.joblib**

	- Can be loaded anytime without retraining:

&nbsp;	

&nbsp;	**from breast\_cancer\_model import load\_model**

	**model = load\_model("breast\_cancer\_model.joblib")**



### SAMPLE PREDICTION :

&nbsp;	sample = test\_x.iloc\[\[0]]

&nbsp;	pred = model.predict(sample)

&nbsp;	print("prediction :",pred\[0]) #2 (benign) or 4 (malignant)



##### AUTHOR :

Sakshi Santosh Kedari

date : 16/08/2025

