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
        total = candidates.values()
        sum_votes = sum(total)
    
        candidates_l = candidates.keys()

#get percent (x/sum)x100 using perc_format      
#     
        votes_per = [f'{(x/sum_votes)*100:.3f}%' for x in candidates.values()]

#find cand. with most amount of votes
       
        winner = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]

        winner
print("Election results")

print("---------------------------")

print(f" Total votes: {int(sum_votes)}")

print("----------------------------")
#for loop per %
j = 0
for candidate, vote in candidates.items():
    print(f'{candidate}, {votes_per[j], (vote)}') 
    j+=1
print("---------------------------")
print(f" Winner: {winner}")
print("------------------------")