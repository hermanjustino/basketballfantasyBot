# importing module
from pandas import *
 
# reading CSV file
data = read_csv("/Users/hermanjustino/Desktop/FantasyBot/players.csv")
 
# converting column data to list
points = data['PTS'].tolist()
rebounds = data['TRB'].tolist()

minutesPlayed = points + rebounds

 
# printing list data
print(minutesPlayed)