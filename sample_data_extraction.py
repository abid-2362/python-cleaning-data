import pandas as pd

# artwork data has been shifted in -- extras folder
# This program will work only if the artwork_data.csv file is also included in the ./data folder
data = pd.read_csv("./data/artwork_data.csv", nrows=500)
data.to_csv("./data/artwork_sample.csv", index=False)
