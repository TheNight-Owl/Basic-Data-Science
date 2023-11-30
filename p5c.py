import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

df=pd.read_csv("heights2.csv")

# print(df.shape)
# print(df.sample(5))         #Any random sample


#Plotting hsitogram
# plt.hist(df["Height"], bins=20)
# plt.show()


#Distplot
# sn.distplot(df["Height"])
# plt.show()


#Getting min, max, mean height, standard deviation
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].mean())
# print(df["Height"].std())



#Finding outlier using 3 standard deviation
lower_limit=df["Height"].mean()-3*df["Height"].std()
upper_limit=df["Height"].mean()+3*df["Height"].std()
# print(lower_limit)
# print(upper_limit)

#The outliers are:-
# print(df[(df["Height"]<lower_limit) | (df["Height"]>upper_limit)])

#Removing the outliers
# print(df[(df["Height"]>lower_limit) & (df["Height"]<upper_limit)])


#outlier shape
outlier=df[(df["Height"]<lower_limit) | (df["Height"]>upper_limit)]
print(outlier.shape)

#Shape of dataframe after removing the outliers
print(df.shape[0]-outlier.shape[0])