import csv
import os
#Assign variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign variable to save file to path
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#Initialize total vote counter
total_votes = 0

#Candidate list
candidate_options = []
#Candidate votes
candidate_votes = {}

#Winner info
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    #Analyze and read data
    file_reader = csv.reader(election_data)

    #read header row
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #Add to total vote counter
        total_votes += 1

        #print candidate name for each row
        candidate_name = row[2]

        #add name to candidate options if it's not included
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #begin tracking candidate votes
            candidate_votes[candidate_name] = 0

        #add vote to candidates count
        candidate_votes[candidate_name] +=1

#save results to text file
with open(file_to_save, "w") as txt_file:

#print final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")

    print(election_results, end = "")
    #save final vote count to text file
    txt_file.write(election_results)

    #Determine the percent of votes for each candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        voting_percentage = float(votes)/float(total_votes) * 100

        #print out each candidate's name, vote count, and percentage of
        #votes to the terminal.
        candidate_results = (
            f"{candidate_name}: {voting_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #save candidate results to text file
        txt_file.write(candidate_results)

        #Determine if the votes are greater than the winning count.
        if (votes>winning_count) and (voting_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = voting_percentage
            winning_candidate = candidate_name

    winning_candidate_summary =(
        f"-----------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"-----------------\n")

    print(winning_candidate_summary)
    #Save winning candidate summary to text file
    txt_file.write(winning_candidate_summary)