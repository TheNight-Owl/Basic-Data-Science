import pandas as pd
from pandas import DataFrame
from sklearn import linear_model as lm
import statsmodels.api as sm


import seaborn as sn
import matplotlib.pyplot as plt

df=pd.read_csv("stock.csv")
# print(df)


x=df[["Interest_Rate"]]
y=df["Stock_Index_Price"]

reg=lm.LinearRegression()
reg.fit(x, y)
# print(reg.fit(x,y))


#Displaying intercept and coefficient
# print(reg.intercept_)
# print(reg.coef_)


#Regplot
# sn.regplot(x=df["Stock_Index_Price"], y=df["Interest_Rate"])
# plt.title("Scatter for Stock_Index_Price Vs Interest_Rate with Regression Line", y=1.05)
# plt.show()


#Prediction of stock price
# print(reg.predict(x))
y_predict=reg.predict(x)
# df1=pd.DataFrame({"Predict Stock Price": y_predict})
# print(df1)



#Prediction using new rate
new_rate=2.09
# print(f"Predict stock index: {reg.predict([[new_rate]])}")



#Corelation coefficient
# print(df[["Interest_Rate", "Stock_Index_Price"]].corr())



#OLS regression results
X=sm.add_constant(x)
model=sm.OLS(y, X).fit()
print(model.summary())
