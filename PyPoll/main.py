# imports
import os
import csv
#from pathlib import Path

# csv reader function
def load_csv(filename):
    # Open file in read mode
    file = open(filename,"r")
    # Reading file
    lines = csv.reader(file)
    next(lines)
    data = list(lines)
    return data
file_path = ("Resources/election_data.csv")
data = load_csv(file_path)
# fuction to convert data
def convert_data(data):
    ballot_id=[]
    candidate_name=[]
    for i in range(len(data)):
        ballot_id.append(int(data[i][0]))
        candidate_name.append(data[i][2])
    return ballot_id,candidate_name

ballot_id,candidate = convert_data(data)
candidate_name= list(set(candidate)) # get the candidates
# print name of candidates
print(candidate_name)

# initialize the counts by each voter
candidate_one_votes = 0
candidate_two_votes = 0
candidate_three_votes = 0
# loop to count total vote by each candidate
for i in range(len(candidate)):
    if candidate[i] == candidate_name[0]:
        candidate_one_votes += 1
    if candidate[i] == candidate_name[1]:
        candidate_two_votes += 1
    if candidate[i] == candidate_name[2]:
        candidate_three_votes += 1

# compute the percentage of each voter
total_votes_casted = len(ballot_id)
candidate_one_percentage = round((candidate_one_votes / total_votes_casted) * 100, 2)
candidate_two_percentage = round((candidate_two_votes / total_votes_casted) * 100, 2)
candidate_three_percentage = round((candidate_three_votes / total_votes_casted) * 100, 2)

# print candidate score and percentage
print(f'total votes casted  {total_votes_casted}')
print(f'votes  by : {candidate_name[0]} is   ({candidate_one_votes}) represents  {candidate_one_percentage} % of total votes')
print(f'votes  by : {candidate_name[1]} is  ({candidate_two_votes}) represents  {candidate_two_percentage} % of total votes')
print(f'votes  by : {candidate_name[2]}  is  ({candidate_three_votes}) represents  {candidate_three_percentage} % of total votes')
# declear the winner of the election with majority vote 
def declare_winner(candidate_one_votes,candidate_two_votes,candidate_three_votes):
    max_vote=max(candidate_one_votes,candidate_two_votes,candidate_three_votes)
    if max_vote == candidate_one_votes:
        print(f'Winner: {candidate_name[0]}')
    if max_vote == candidate_two_votes:
        print(f'Winner: {candidate_name[1]}')
    if max_vote == candidate_three_votes:
        print(f'Winner: {candidate_name[2]}')

declare_winner(candidate_one_votes,candidate_two_votes,candidate_three_votes)