import os
import csv

#list of canditates
candidates = {}


#path
csvpath = os.path.join("..", "Resources", "PyPoll_Resources_election_data.csv")

with open(csvpath, 'r') as csvfile:
#read csv
    csvreader = csv.reader(csvfile, delimiter=',')
#skip header
    header = next(csvreader)
#for loop for total amount of votes using keys method
for row in csvreader:
        if row[2] in candidates.keys():
            candidates[row[2]]+=1
        else:
            candidates[row[2]] = 1