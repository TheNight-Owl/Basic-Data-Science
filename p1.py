import pandas as pd
df=pd.read_csv("IPL dataset1.csv")

#display the type
# print(type(df))


#Show number of rows & columns as tuple
# print(df.shape)


#To show top 'n' rows. If 'n' is -ve all rows except last 'n' rows will be shown. Default 5 rows
# print(df.head(-3))



#To show bottom 'n' rows. If 'n' is -ve all rows except first 'n' rows will be shown. Default 5 rows
# print(df.tail(-5))


#To display all column names as a list
# print(df.columns)


pd.set_option("display.max_columns", 5)


#To transpose
# print(df.transpose())
# print(df.head().transpose())


#Information about dataframe
# print(df.info())


# Index based extraction with and without fields
# print(df[2:6])
# print(df[-12:-6])
# print(df[["AGE", "SIXERS"]][2:19:2])


#Extraction based on index of rows as well as columns of an index range
# print(df.iloc[5:10, 4:8])


#To count the number of values
# print(df.value_counts(["AGE", "SIXERS"]))
# print(df.AGE.value_counts(normalize=True))


#Cross tabulation
# print(pd.crosstab(df["AGE"], df["TEAM"]))


#Sorting values
# print(df[["AGE", "BASE PRICE"]].sort_values("BASE PRICE", ascending=False))


#Creating new columns
df["PREMIUM"]=df["SOLD PRICE"]-df["BASE PRICE"]
# print(df["PREMIUM"])
# print(df[["PLAYER NAME", "PREMIUM"]].sort_values("PREMIUM", ascending=False)[0:8].reset_index())


#Renaming Columns
# df.rename(columns={"AGE": "P_AGE"}, inplace=True)
# print(df[5:10])


#Removing column
# print(df.shape)
# df.drop("PLAYER NAME", axis="columns", inplace=True)
#Multiple columns removal
# df.drop(["PLAYER NAME", "SIXERS"], axis="columns", inplace=True)
# print(df.shape)


#Removing rows (if axis is not specified then rows are automatically targeted)
# print(df.shape)
# df.drop([5,10], axis="index", inplace=True)
# print(df.shape)
#Removing rows of a specified range
# df.drop(df.index[5:10], axis="index", inplace=True)
# print(df.shape)


#Applying Conditions
# print(df[df["SIXERS"]>80][["PLAYER NAME", "SIXERS"]])


#Deleting based on condition
# print(df.shape)
# df.drop(df[df["SIXERS"]>80].index, inplace=True)
# print(df.shape)


#Groupby
# print(df.groupby("AGE")["BASE PRICE"].max())
# print(df.groupby(["AGE", "PLAYING_ROLE"])["BASE PRICE"].min())


# #Merging DataFrames
# t1=df.groupby("AGE")["SOLD PRICE"].max().reset_index()
# t2=df.groupby(["AGE", "PLAYING_ROLE"])["SOLD PRICE"].max().reset_index()
# print(t1, t2)
# print(type(t1))
# t3=t1.merge(t2, on="AGE", how="outer")
# print(t3)



# =========================================================
# Creating a new DataFrame
df1=pd.DataFrame({"B_Id": ["B1", "B2", "B3", "B4"], "Colour": ["RED", "BLACK", "BLUE", "GREEN"]})
df2=pd.DataFrame({"B_Id": ["B1", "B2", "B3", "B4"], "S_Id": ["S1", "S2", "S3", "S4"]})
print(df1)
print(df2)

#Performing merge on these 2 DataFrames
# df3=pd.merge(df1, df2, on="B_Id")
df3=pd.merge(df1, df2, on="B_Id", how="right")
print(df3)