import string
import pandas as pd
pd.options.display.float_format = "{:,.2f}".format

#2022-23 projections dataset
data = pd.read_csv("/Users/hermanjustino/Desktop/FantasyBot/players.csv")

#pergame data set
perGame = pd.read_csv("/Users/hermanjustino/Desktop/FantasyBot/perGame.csv")

#make turnovers a negative value
data['TOV'] = data['TOV'] * -1
perGame['TOV'] = perGame['TOV'] * -1

source_cols = data.columns

columnTotal = source_cols



#mintes played per game with player dataset based on 2021-22 Per game
minutes = pd.read_csv("/Users/hermanjustino/Desktop/FantasyBot/perGame.csv", usecols = ['Player','MP'])

cols = ['TRB', 'AST', 'FG', 'PTS', '3P', 'FT', 'TOV', 'BLK', 'STL']

#define new column that contains sum of specific columns
data['sum_stats'] = data[cols].sum(axis=1)


#data['sum_stats'] = data.sum(axis=1)

#Join projected dataset with 2021-22 minutes played
mindf = pd.merge(data,minutes,on=['Player','Player'],how='left')


mindf['TOV'] = mindf['TOV'] * -1

#sort rows by the cumulative stats
mindf = mindf.sort_values(by=['sum_stats'], ascending=False)

mindf['TOV'] * -1


#the top 10 players(grouped by points), with 2022-23 projections. With 2021-22 minutes played
selection = mindf[['Player', 'PTS', 'AST', 'TRB', 'FG','FG%', '3P', '3P%', 'FT','FT%','BLK', 'STL', 'TOV', 'MP']]
print(selection.head(10))

expected = selection.copy(deep=True)

#Add expected PTS per game column based on 2022-23 projection, and minutes played in 2021-22
expected['exp_PTS'] = (expected['PTS']/36) * expected['MP']
expected['exp_AST'] = (expected['AST']/36) * expected['MP']
expected['exp_TRB'] = (expected['TRB']/36) * expected['MP']
expected['exp_FG'] = (expected['FG']/36) * expected['MP']
expected['exp_3P'] = (expected['3P']/36) * expected['MP']
expected['exp_FT'] = (expected['FT']/36) * expected['MP']
expected['exp_BLK'] = (expected['BLK']/36) * expected['MP']
expected['exp_STL'] = (expected['STL']/36) * expected['MP']
expected['exp_TOV'] = (expected['TOV']/36) * expected['MP'] * -1

expectedPerGame = expected[['Player', 'exp_PTS', 'exp_AST', 'exp_TRB', 'exp_FG','FG%', 'exp_3P','3P%', 'exp_FT','FT%', 'exp_BLK','exp_STL', 'exp_TOV']]

columns = ['exp_PTS', 'exp_AST', 'exp_TRB', 'exp_FG','FG%', 'exp_3P','3P%', 'exp_FT','FT%', 'exp_BLK','exp_STL', 'exp_TOV']
expectedPerGame['cum_stats'] = expectedPerGame[columns].sum(axis=1)
expectedPerGame.sort_values(by=['cum_stats'],ascending=False)

print(expectedPerGame.head(20))

# filtering the rows by player name
selectedName = expectedPerGame[expectedPerGame['Player'].str.contains('Barnes')]

