import pandas as pd

data = pd.read_csv("./data/artwork_data.csv", nrows=10)
data.to_csv("./data/artwork_sample.csv", index=False)
