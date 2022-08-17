import csv

# opening the CSV file
with open('/Users/hermanjustino/Desktop/FantasyBot/players.csv', mode ='r')as file:

    csvFile = csv.reader(file)
    

# displaying the contents of the CSV file
    for lines in csvFile:

        print(lines)