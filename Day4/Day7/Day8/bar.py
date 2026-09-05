import matplotlib.pyplot as plt

students= ['Sam','Amit','Shafiya','Sheru']
marks = [50,100,70,55]

plt.bar(students,marks,color="hotpink",width = 0.2)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Result")
plt.show()