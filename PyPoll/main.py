#David Fried
#Data Science Bootcamp
#6/20/20

#Challenge 2: Modernize a voting process
#election_data.csv
#The dataset is composed of three columns: Voter ID, County, and Candidate
#Python script analyzes the votes and calculates each of the following:
#   The total number of votes cast
#   A complete list of candidates who received votes
#   The percentage of votes each candidate won
#   The total number of votes each candidate won
#   The winner of the election based on popular vote.

import csv
import os

resources = os.path.join('Resources','election_data.csv')
analysis = os.path.join('analysis', 'analysis.txt')

#Converting rows in election CSV file into Py lists
voter_id = []
county = []
candidate = []
with open(resources) as election_data:
    reader = csv.reader(election_data, delimiter=',')
    header = next(reader) #Save CSV header
    for row in reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#Candidate list
candidate_list = []
for name in candidate:
    if name not in candidate_list:
        candidate_list.append(name)

#Number of votes for each candidate, and the percentage of total votes for each candidate
candidate_votes = {}
for name in candidate_list:
    votes = candidate.count(name)
    candidate_votes[name] = f'{votes/len(candidate)*100:.3f}%', votes

#Winner
total = 0
winner = ""
for name,count in candidate_votes.items():
    if count[1] > total:
        total = count[1]
        winner = name

#Election Results - Terminal Output
print('\nElection Results\n------------------------------')
print('Total Votes: {:,}\n------------------------------'.format(len(voter_id)))
for name,count in candidate_votes.items():
    print(f'{name+":":10} {count[0]:>8} ({count[1]:>9,})')
print('Winner: ' + str(winner))

#Election Results - Text Output ('analysis.txt')
with open(analysis, 'w') as analysis:
    analysis.write('Election Results\n------------------------------')
    analysis.write(f'\nTotal Votes: {len(voter_id):,}\n------------------------------')
    for name,count in candidate_votes.items():
        analysis.write(f'\n{name+":":10} {count[0]:>8} ({count[1]:>9,})')
    analysis.write('\nWinner: ' + str(winner))