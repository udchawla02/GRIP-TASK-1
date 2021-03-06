
"""GRIPtask1.ipynb
# **TASK #1 GRIP March 2021**
## **DATA SCIENCE AND BUSINESS ANALYTICS**
## **Prediction using Supervised ML**
### Predict the percentage of an student based on the no. of study hours.
###What will be predicted score if a student studies for 9.25 hrs/ day?
### implemented by:- **UDIT CHAWLA**
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

"""#### Reading Data"""

data=pd.read_csv("https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv")

data

"""#### Analysis of DATA"""

data.info()

data.describe()

data.isnull().sum()

plt.boxplot(data)     ##Data Visualisation
plt.show()

data.plot(x='Hours', y='Scores', style='^', color='red')
plt.title('Hours vs Score')
plt.xlabel('Study Hours')
plt.ylabel('Percentage')
plt.show()

data_scores = data['Scores']
plt.boxplot(data_scores)
plt.title('Box plot for hours vs Scores')
plt.xlabel('Scores')
plt.ylabel('Scores based on no. of hours')
plt.show()

sns.distplot(data['Scores'])

correlation = data.corr(method= 'pearson')
print(correlation)

sns.pairplot(data)



"""# **SIMPLE LINEAR REGRESSION** """

X = data.iloc[:,:-1].values
Y = data.iloc[:,1].values
print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.80, test_size= 0.20, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, Y_train)
print("Training complete")

print("B0 =",regressor.intercept_, "\nB1 =", regressor.coef_)

reg_line = regressor.intercept_ + regressor.coef_*X_train

plt.scatter(X_train, Y_train, color =  'red', marker='.' )
plt.plot(X_train,reg_line,color='yellow')
plt.title("Regression line(training set)")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.show()

import statsmodels.api as sm
x_train_sm = sm.add_constant(X_train)   ##Build linear model
model = sm.OLS(Y_train, x_train_sm).fit()
model.summary()

y_pred = regressor.predict(X_test)
print(y_pred)

df = pd.DataFrame({'Actual': Y_test, 'Predicted': y_pred})
df

plt.scatter(X_test, Y_test, color =  'green', marker='*' )
plt.plot(X_train,reg_line,color='pink')
plt.title("Regression line(testing set)")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.show()

from sklearn import metrics
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

metrics.r2_score(Y_test, y_pred)

MSE = metrics.mean_squared_error(Y_test, y_pred)
RMSE = np.sqrt(MSE)
print("MSE = ", MSE)
print("RMSE = ", RMSE)

Predicted_score = regressor.predict([[9.25]])
print("Predicted score of a student studying 9.25 hours per day is: ", Predicted_score)

"""#**RESULT:-** 
### 1) THE DATA HAVE 2 ATTRIBUTES "Hours" and "Scores
### 2) I HAVE USED "Linear Rgression" BECAUSE "Hours" and "Scores" ARE LINEARLY DEPENDENT
### 3) USING LINEAR REGRESSION I HAVE ACHIEVED 95% Accuracy on the TRAIN SET and 94.54% Accuracy on the TRAIN DATA
### 4) WE CAN CONCLUDE THAT OUR MODEL IS NOT OVERFITTING
### **5) IF A STUDENT STUDIES FOR 9.25 HOURS A DAY THE PREDICTED SCORE WILL BE 93.69** 


"""

