import matplotlib.pyplot as plt


#Plotting a point
# plt.plot(3, 2, "rp")
# plt.show()

#Plotting a set of points (just a line)
# plt.plot([2,3,4],[4,6,8])
# plt.show()


#Plotting a set of points (just the points)
# plt.plot([2,3,4],[4,6,8], "ro")
# plt.show()


#Plotting a set of points (points with the line)
# plt.plot([2,3,4],[4,6,8], "ro--")
# plt.show()


#Plotting random points
# plt.plot([1,2,3,4], "ro--")
# plt.show()


#Plotting points with marker size & linewidth
# plt.plot([2,3,4],[4,6,8], "ro--", markersize=10, linewidth=5)
# plt.show()


#Plotting multiple lines
# plt.plot([1,2,3],[1,2,3])
# plt.plot([4,5,6],[4,5,6])
# plt.show()


#Plotting labels, title and grid
# plt.plot([4,5,6],[4,5,6], "bo--")
# plt.xlabel("X ->")
# plt.ylabel("Y ->")
# plt.grid()
# plt.title("Random graph")
# plt.show()


#Bar chart (vertical)
# plt.bar(["A", "B", "C", "D"], [10,20,30,40])
# plt.show()


#Bar chart (horizontal)
# plt.barh(["A", "B", "C", "D"], [10,20,30,40])
# plt.show()


#Bar chart (horizontal with color)
# plt.barh(["A", "B", "C", "D"], [10,20,30,40], color="magenta")
# plt.show()


#Bar chart (setting bar width. default bar width=0.8)
# plt.bar(["A", "B", "C", "D"], [10,20,30,40], width=0.3)
# plt.show()

# ==========================================
# ==========================================
# ==========================================

import seaborn as sn
import pandas as pd
df=pd.read_csv("IPL dataset1.csv")

# d1=pd.DataFrame({"Country":["India", "Rome", "Italy"], "Population":[2000, 1800, 1660]})
# print(d1)
# sn.barplot(d1, x="Country", y="Population")
# plt.show()

# sn.barplot(data=d1, x="Country", y="Population")
# plt.show()

# d=df.groupby("AGE")["SOLD PRICE"].mean().reset_index()
# # sn.barplot(x="AGE", y="SOLD PRICE", data=d)
# # plt.title("Avg. sp vs Age")
# # plt.xlabel("Age")
# # plt.ylabel("Avg. sp")
# # plt.show()


#Density plot
# sn.displot(df["AGE"])
sn.distplot(df["AGE"])
plt.show()


#Histogram (default no. of bins=10)
# plt.hist(df["SOLD PRICE"], bins=20)
# plt.ylabel("Frequency")
# plt.xlabel("SOLD PRICE")
# plt.show()