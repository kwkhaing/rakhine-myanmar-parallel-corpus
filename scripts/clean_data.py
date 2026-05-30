import pandas as pd

df = pd.read_csv("data/train.csv")

# remove empty rows
df = df.dropna()

# remove duplicates
df = df.drop_duplicates()

# strip spaces
df["rakhine"] = df["rakhine"].str.strip()
df["myanmar"] = df["myanmar"].str.strip()

df.to_csv("data/train_clean.csv", index=False)
