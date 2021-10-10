
# Add our dependencies.
import csv # reading files
import os #  reading path

# Assign a variable for the file to load and the path.
dir_path = os.path.dirname(os.path.realpath(__file__)) #  getting the directory of the current program 
os.chdir(dir_path)# changes the current directiory to program directory path 

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
#  Declare the empty dictionary.
candidate_votes = {}
# an empty string value for the winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #  Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
           # Begin tracking that candidate's vote count. setting each candidate's vote count to zero
            candidate_votes[candidate_name] = 0 
        # Add a vote to that candidate's count. This has to line up witht he if or it wont work.
        candidate_votes[candidate_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")          
    # Determine the percentage of votes for each candidate by looping through the counts.
    #  Iterate through the candidate list.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        for candidate_name in candidate_votes:
        #  Retrieve vote count of a candidate.
         votes = candidate_votes[candidate_name]
        #  Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)  
         # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            #  To do: print out the winning candidate, vote count and percentage to
             #   terminal.
            winning_candidate_summary = (
                 f"-------------------------\n"
                 f"Winner: {winning_candidate}\n"
                 f"Winning Vote Count: {winning_count:,}\n"
                 f"Winning Percentage: {winning_percentage:.1f}%\n"
                 f"-------------------------\n")
            print(winning_candidate_summary)
            # Open the election results and read the file.
            with open(file_to_load) as election_data:
        # To do: read and analyze the data here.
    # Read the file object with the reader function.
                file_reader = csv.reader(election_data)#allow us to read the CSV
    # Print the header row.
                headers = next(file_reader)
                print(headers)    


    # Create a filename variable to a direct or indirect path to the file.
    file_to_save = os.path.join("analysis", "election_analysis.txt")
    # Using the open() function with the "w" mode we will write data to the file.
    #open(file_to_save, "w")
    # Using the with statement open the file as a text file.
    with open(file_to_save, "w") as txt_file:
        
        # Write some data to the file.
        #txt_file.write("Arapahoe, Denver, Jefferson")
    # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)