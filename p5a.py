#Range
x=[10,20,30,40,50,60]
# print(f"Range is {max(x)-min(x)}")


#Finding q1, q3, iqr, qd (Even dataset)
import statistics as st

# data=[32,36,46,47,56,69,75,79,79,88,89,91,92,93,96,97,101,105,112,116]
# q1=st.median(data[:10])
# q3=st.median(data[10:])
# iqr=q3-q1
# qd=iqr/2
# print(f"q1={q1}")
# print(f"q3={q3}")
# print(f"iqr={iqr}")
# print(f"qd={qd}")


#Finding q1, q3, iqr, qd (Odd dataset)
# data=[32,36,46,47,56,69,75,79,79,88,89,91,92,93,96,97,101,105,112]
# q1=st.median(data[:9])
# q3=st.median(data[10:])
# iqr=q3-q1
# qd=iqr/2
# print(f"q1={q1}")
# print(f"q3={q3}")
# print(f"iqr={iqr}")
# print(f"qd={qd}")


#Mean deviation about mean
import numpy as np
from numpy import mean, absolute
# data=[5,12,1,0,4,22,15,3,9]
# result=mean(absolute(data-mean(data)))
# print(result)
# print(round(result, 2))


#Mean deviation about median
# data=[8,15,53,49,19,62,7,15,95,77]
# # result=mean(np.abs(data-np.median(data)))
# result=mean(absolute(data-np.median(data)))
# print(result)



#Standard deviation
# speed=[86,87,88,86,87,85,86]
# print(np.std(speed))
# print(round((np.std(speed)), 3))


#Variance
speed=[32,111,138,28,59,77,97]
print(np.var(speed))
print(round((np.var(speed)), 3))
