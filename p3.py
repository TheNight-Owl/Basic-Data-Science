import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

df=pd.read_csv("IPL dataset1.csv")

#Scatter plot
# plt.scatter([5,7,8,7,2,17,2,9,4,11,12,9,6],[99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.show()

# plt.scatter([5,7,8,7,2,17,2,9,4,11,12,9,6],[99,86,87,88,111,86,103,87,94,78,77,85,86], color="blue")
# plt.scatter([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12],[100,105,84,105,90,99,90,95,94,100,79,112,91,80,85], color="green")

# # plt.grid(axis="x")
# # plt.grid(axis="y")
# plt.grid(axis="y", linewidth=3, color="red", linestyle="--")
# plt.show()


#scatter plot for dataframe
# part_of_dataframe=df[df["PLAYING_ROLE"]=="Batsman"]
# print(part_of_dataframe["SIXERS"])
# print(part_of_dataframe["SOLD PRICE"])

# plt.scatter(x=part_of_dataframe["SIXERS"], y=part_of_dataframe["SOLD PRICE"])
# plt.title("Scatter plot for SOLD PRICE VS SIXERS")
# plt.ylabel("SOLD PRICE")
# plt.xlabel("SIXERS")
# plt.show()


#Scatter plot with regplot
# sn.regplot(x=part_of_dataframe["SIXERS"], y=part_of_dataframe["SOLD PRICE"])
# plt.title("Scatter plot for SOLD PRICE VS SIXERS with regplot", y=1.05) #y is used to move the title a bit up or low
# plt.ylabel("SOLD PRICE")
# plt.xlabel("SIXERS")
# plt.show()


#LineWidth
# plt.plot([1,2,3,4,5], linewidth=6)
# plt.show()


#subplot
#Here titles are overlapping
# plt.subplot(2,2,1)
# plt.title("Fig. 1")
# plt.plot([1,2,3],[4,5,6])

# plt.subplot(2,2,2)
# plt.title("Fig. 2")
# plt.plot([10,20,30],[40,50,60])

# plt.subplot(2,2,3)
# plt.title("Fig. 3")
# plt.plot([100,200,300],[400,500,600])

# plt.subplot(2,2,4)
# plt.title("Fig. 4")
# plt.plot([70,28,39],[4,50,6])

# plt.show()


# subplots_adjust (To adjust the spaces)
# plt.subplot(2,2,1)
# plt.title("Fig. 1")
# plt.plot([1,2,3],[4,5,6])

# plt.subplot(2,2,2)
# plt.title("Fig. 2")
# plt.plot([10,20,30],[40,50,60])

# plt.subplots_adjust(hspace=3)   #hspace stands for height space

# plt.subplot(2,2,3)
# plt.title("Fig. 3")
# plt.plot([100,200,300],[400,500,600])

# plt.subplot(2,2,4)
# plt.title("Fig. 4")
# plt.plot([70,28,39],[4,50,6])

# plt.show()



#====================================
#====================================
influential_features=["SR_B", "AVE", "SIXERS", "SOLD PRICE"]
# sn.pairplot(df[influential_features])
# plt.show()


#corelation
# print(df[influential_features].corr())


#heatmap
# sn.heatmap(df[influential_features].corr())
# sn.heatmap(df[influential_features].corr(), annot=True)
# plt.title("Heatmap", y=1.5)
# plt.show()


#Boxplot
box=sn.boxplot(df["SOLD PRICE"])
# plt.show()


box1=plt.boxplot(df["SOLD PRICE"])
# plt.show()

# print(box)
# print(box1)

print([item.get_ydata()[0] for item in box1["caps"]])
print([item.get_ydata()[0] for item in box1["whiskers"]])
print([item.get_ydata()[0] for item in box1["medians"]])