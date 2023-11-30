import pandas as pd
df=pd.read_csv("heights1.csv")


#Getting Q1 and Q3 from the dataset
q1=df.height.quantile(0.25, interpolation="midpoint")
q3=df.height.quantile(0.75, interpolation="midpoint")
# print(q1)
# print(q3)

iqr=q3-q1
# print(iqr)


#lower and upper limits
lower_limit=q1-1.5*iqr
upper_limit=q3+1.5*iqr
# print(lower_limit)
# print(upper_limit)


#Get the outliers
# print(df[(df["height"]<lower_limit) | (df["height"]>upper_limit)])


#Showing the dataset after removing outliers
print(df[(df["height"]>lower_limit) & (df["height"]<upper_limit)])