# Path to the file
import csv
import os
file_to_load = os.path.join('C:/','Users','Dell PC','Election_Analysis','Resources','election_results.csv')
file_to_save = os.path.join('C:/','Users','Dell PC','Election_Analysis','analysis','election_analysis.txt')
# Empty strings
largest_county_turnout = None
winning_candidate = None
# Counters
county_total_votes = 0
county_winning_count = 0
county_winning_percentage = 0
candidate_total_votes = 0
candidate_winning_count = 0
candidate_winning_percentage = 0
# Lists
county_options = []
candidate_options = []
# Dictionaries
county_votes = {}
candidate_votes = {}



# Open csv file to read
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        # County votes counter
        county_total_votes += 1        
        county_name = row[1]
        if county_name in county_options:  
            county_votes[county_name] += 1 
        elif county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
            county_votes[county_name] += 1
        # Candidate votes counter
        candidate_total_votes += 1        
        candidate_name = row[2]
        if candidate_name in candidate_options:  
            candidate_votes[candidate_name] += 1 
        elif candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] += 1



# Open text file to write
with open(file_to_save, "w") as txt_file:
    # Print election results
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {county_total_votes:,}\n"
        f"-------------------------\n"
        )
    print(election_results, end="")
    txt_file.write(election_results)



    # Calculate and print county results
    print("\nCounty Votes:")
    txt_file.write("\nCounty Votes:\n")    
    for county in county_votes:
        votes = county_votes[county]
        vote_percentage = float(votes) / float(county_total_votes) * 100
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results, end="")
        txt_file.write(county_results)
    # Determine and print largest county turnout
        if (votes > county_winning_count) and (vote_percentage > county_winning_percentage):
            county_winning_count = votes
            largest_county_turnout = county
            county_winning_percentage = vote_percentage
    largest_county_summary = (
        f"--------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"--------------------------\n")
    print(largest_county_summary)
    txt_file.write(largest_county_summary)



    # Calculate and print candidate results
    print("Candidate Votes:")
    txt_file.write("\nCandidate Votes:\n")
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(candidate_total_votes) * 100 
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results, end="")
        txt_file.write(candidate_results)
    # Determine and print winning candidate summary
        if (votes > candidate_winning_count) and (vote_percentage > candidate_winning_percentage):
            candidate_winning_count = votes
            winning_candidate = candidate
            candidate_winning_percentage = vote_percentage 
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {candidate_winning_count:,}\n"
        f"Winning Percentage: {candidate_winning_percentage:.1f}%\n"
        f"--------------------------\n"
        )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)