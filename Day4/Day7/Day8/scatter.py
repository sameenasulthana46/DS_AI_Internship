import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]
sizes=[100,20,40,30,100]

plt.scatter(x,y,s=sizes)
plt.show()