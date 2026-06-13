import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://www.football-data.co.uk/mmz4281/2526/E0.csv"

df = pd.read_csv(url)

print(df.shape)
print(df.columns.tolist())
print(df.head())
