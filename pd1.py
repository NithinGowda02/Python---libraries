import pandas as pd

data = {
    "Name" :["Nithin K P", "Rahul", "Madan", "Gagan"],
    "Age" : [23, 21, 21, 20],
    "City" : ["Somwarpet", "Mysore", "Mandya", "Mysore"]
}

df = pd.DataFrame(data)
df.to_json("output.json", index=False)