import pandas as pd

data = {
    "Name" : ["Nithin K P", "Gagan L R", "Madan G R", "Manvith M N", "Deekshith", "Sanjay"," Ravi kiran", "Arjun M"],
    "Age" : [23, 21, 22, 30, 35, 23, 26, 29],
    "Salary" : [50000, 35000, 40000, 46000, 69000, 75000, 56000, 60000],
    "Performance_score" : [85, 79, 68, 77, 89, 95, 98, 70]
}

df = pd.DataFrame(data)

#print(df[["Name","Salary"]])
#print(df[df["Salary"] > 50000])
#print(df[(df["Salary"] > 50000) & (df["Age"] > 25)])
print(df[(df["Salary"] > 50000) | (df["Age"] > 25)])