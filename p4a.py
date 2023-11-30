import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd

df=pd.read_csv("IPL dataset1.csv")
# print(df.head())



#outlier detection using boxplot
# print(df[df["SOLD PRICE"]>1350000][["PLAYER NAME", "PLAYING_ROLE", "SOLD PRICE"]])


#Comparing distributions
# sn.distplot(df[df["CAPTAINCY_EXP"]==1]["SOLD PRICE"], color="red", label="Captaincy expericence")
# sn.distplot(df[df["CAPTAINCY_EXP"]==0]["SOLD PRICE"], color="green", label="No captaincy expericence")
# plt.legend()
# plt.show()


#Boxplot of sold price for different playing roles
# sn.boxplot(x=df["PLAYING_ROLE"], y=df["SOLD PRICE"])
# plt.title("Boxplot of sold price for different playing roles")
# plt.show()



#===================================
#===========Pie charts==============
#===================================

# plt.pie([25,50,75,100])
# plt.pie([25,50,75,100], labels=["Cricket", "Football","Volleyball","Basketball"])
# plt.pie([25,50,75,100], labels=["Cricket", "Football","Volleyball","Basketball"], autopct="%.2f")
# plt.pie([25,50,75,100], labels=["Cricket", "Football","Volleyball","Basketball"], autopct="%.2f%%")
# plt.pie([25,50,75,100], labels=["Cricket", "Football","Volleyball","Basketball"], colors=["red", "green", "blue", "yellow"], autopct="%.2f%%")
# plt.title("Pie Chart")
# plt.show()

plt.pie([25,50,75,100], labels=["Cricket", "Football","Volleyball","Basketball"], colors=["red", "green", "blue", "yellow"], autopct="%.2f%%")
plt.title("Pie Chart")
# plt.axis("equal")
plt.legend(loc="lower left")
plt.show()