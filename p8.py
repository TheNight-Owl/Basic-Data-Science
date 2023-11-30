import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("insurance_data.csv")
# print(df)


# plt.scatter(x=df["age"], y=df["bought_insurance"], color="red", marker="+")
# plt.show()


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(df[["age"]], df["bought_insurance"], train_size=0.9)
# print(x_train)


from sklearn import linear_model as lm
reg=lm.LogisticRegression()
reg.fit(x_train, y_train)


#intercept and coefficient
# print(reg.intercept_)
# print(reg.coef_)


#predict
# print(reg.predict(x_test))

#score
# print(reg.score(x_test, y_test))



#Changing train_size from 0.9 to 0.8
x_train, x_test, y_train, y_test=train_test_split(df[["age"]], df["bought_insurance"], train_size=0.8)
# print(x_train)

print(reg.intercept_)
print(reg.coef_)

import math
def sigmoid(n):
    return 1/(1+math.exp(-n))

def prediction_function(n):
    # y=mx+c
    y=(0.12461623*n)+(-4.97886403)
    z=sigmoid(y)
    return z

ans=prediction_function(66)
print(ans)