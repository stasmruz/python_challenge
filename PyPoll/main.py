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
