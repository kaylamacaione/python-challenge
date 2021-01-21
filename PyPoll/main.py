import os
import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    #define variables
    TotalVotes = 0
    CandidatesUnique = []
    CandidateVoteCount = []
    

    for row in csvreader:

    #Find total number of votes cast
        TotalVotes += 1

    #Find complete list of candidates who received votes
        Candidate = (row[2])

        if Candidate in CandidatesUnique:
            CandidateIndex = CandidatesUnique.index(Candidate)
            CandidateVoteCount[CandidateIndex] = CandidateVoteCount[CandidateIndex] + 1

        else:
            CandidatesUnique.append(Candidate)
            CandidateVoteCount.append(1)
    

#Find percentage of votes each candidate won and total number of votes each candidate won + find winner

Percent = []
MaxVotes = CandidateVoteCount[0]
MaxIndex = 0

for Candidate in range(len(CandidatesUnique)):
    VotePercent = round(CandidateVoteCount[Candidate]/TotalVotes*100)
    Percent.append(VotePercent)

    if CandidateVoteCount[Candidate] > MaxVotes:
        MaxVotes = CandidateVoteCount[Candidate]
        MaxIndex = Candidate

    Winner = CandidatesUnique[MaxIndex]
    



print("Election Results")
print("---------------------------") 
print("Total Votes:" + str(TotalVotes))
print("---------------------------") 
for Candidate in range(len(CandidatesUnique)):
    print(f'{CandidatesUnique[Candidate]} : {Percent[Candidate]}% ({CandidateVoteCount[Candidate]})')
print("---------------------------") 
print(f'Election Winner: {Winner}')


#output files
output_file = os.path.join('Analysis','PyPoll_Analysis.txt')

file = open('Analysis/PyPoll_Analysis.txt','w')

file.write("Election Results\n")
file.write("---------------------------\n")
file.write(f"Total Votes:" + str(TotalVotes) + "\n")
for count in range(len(CandidatesUnique)):
    file.write(f"{CandidatesUnique[Candidate]}: {Percent[Candidate]}% ({CandidateVoteCount[Candidate]})\n")
file.write("---------------------------\n")
file.write(f"Winner: {Winner}\n")