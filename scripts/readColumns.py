# importing the module
import pandas as pd
  
# read specific columns of csv file using Pandas

df = pd.read_csv("/Users/hermanjustino/Desktop/FantasyBot/players.csv", usecols = ['Player','TRB','3P%'])

print(df)
