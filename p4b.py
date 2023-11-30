#============================
#Various statistical measures
#============================

import statistics as st

#Mean of simple data
print(st.mean([1,2,3,4,5,6]))
print(st.mean([-10,23,56,84,-987,58]))
print(round(st.mean([-10,23,56,84,-987,58]), 3))


#Median of simple data
print(st.median([1,2,1,2,1,2,3]))
print(st.median([100,65,-2,87,65]))


#Mode for a given set of data
print(st.mode([1,1,2,2,2,3,3,3]))       #Gives only one value that is at first if 2 observations have same no. of occurrences


print(st.multimode(["red", "red", "red", "blue"]))
print(st.multimode([1,1,2,2,2,3,3,3]))


#Operations on DataFrames
import pandas as pd

df=pd.DataFrame({'team':['A','A','A','A','B','B','B','B'], 'position':['G', 'F','F','G','F','F','G','G'], 'points':[30,22,19,14,14,11,20,28], 'assists':[4,3,7,7,12,15,8,4]})
print(df)

#Mean
print(df.groupby("team")[["points", "assists"]].mean())

#Median
print(df.groupby("team")["points"].median())