import pandas as pd
from sklearn import linear_model as lm
import statsmodels.api as sm
import numpy as np


df=pd.read_csv("stock.csv")
# print(df)

reg=lm.LinearRegression()
x=df[['Interest_Rate', 'Unemployment_Rate']]
y=df['Stock_Index_Price']
reg.fit(x, y)


#Displaying intercepts and coefficients
# print(reg.intercept_)
# print(reg.coef_)



#Prediction with sklearn
new_interest_rate=2.75
new_unemployment_rate=5.3
# print(reg.predict([[new_interest_rate, new_unemployment_rate]]))



#OLS model
X=sm.add_constant(x)
model=sm.OLS(y, X).fit()
# print(model.summary())



#Prediction
y_pred=reg.predict(x)
df1=pd.DataFrame({"Predicted Stock Index Price":y_pred})
# print(df1)


#Residuals
residuals=y-y_pred
# print(residuals)


#Observation with largest positive residual
# print(max(residuals))       #Gives the value
# print(np.argmax(residuals))     #Gives the index of the max residual. Add 1 to it for exact index(if we count from 1 and not 0)



#Mean and median of residuals
# print(np.mean(residuals))
# print(np.median(residuals))



#Correlation of residuals with target values
# print(np.corrcoef(residuals, y)[0,1])



#Correlation of residuals with fitted values
print(np.corrcoef(residuals, model.predict(X))[0,1])