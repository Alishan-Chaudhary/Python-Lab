import pandas as pd

file_path = "csvfile.csv"
df = pd.read_csv(file_path)
print(df)

filetr_mask = (df["name"]== "alishan")
print(df[filetr_mask])