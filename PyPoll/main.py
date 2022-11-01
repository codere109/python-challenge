#CODE INSPIRED BY STUDENT & TA

import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')



# Initialize the 'Total Vote' count and the 'Winning' count. 
total_votes = 0
winner_count = 0
# Initialize the list of candidates. 
candidates = []
# Initialize the dictionary of candidates and their votes. 
candid_votes = {}



with open(csvpath) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")


    
    
  
    # # candidate1 = {f'Name': 'Charles Casper Stockham',
    # # 'Percentage': {},
    # # 'Votes': {}}
   
    # # candidate2 =  {f'Name': 'Diana DeGette',
    # # 'Percentage': {},
    # # 'Votes': {}}
  
    # # candidate3 = {'Name': 'Raymon Anthony Doane',
    # # 'Percentage': {},
    # 'Votes': {}}
    
    
    
    
    
    

# Skipping the header row. 
    header_row = next(csv_file)
# Iterating through the rows in the election data file. 
    for row in csvreader:
        # Identifying the rows of candidates in the eletion data file. 
        candid_name = row[2]
        # Incrementing the total vote count for each row in the election data file. 
        total_votes = total_votes + 1
        # Adding a new candidate name to a list for every row in the election data file. 
        if candid_name not in candidates:
            candidates.append(candid_name)
            # Initializing the vote count for each new candidate name. 
            candid_votes[candid_name] = 0
        # Adding to the vote count of every candidate name if similar. 
        candid_votes[candid_name] += 1
# Writing the first part of the results of the analysis. 
first_result = str(f"Election Results\n"
                    f"------------------\n"
                    f"Total Votes: {total_votes}\n"
                    f"------------------"
                    )
# Initializing the add-on to the second part of the analysis results. 
results = ""
# Initiating a for loop for the 'Candidate Votes' dictionary. 
for candid_name, votes in candid_votes.items():
    # Calculating the percentage of votes cast for each candidate. 
    vote_percentage = votes / total_votes
    # Formatting the vote percentage of each candidate to have three decimal places and a percentage sign. 
    vote_percentage_formatted = "{:.3%}".format(vote_percentage)
    # Writing the second part of the analysis results. 
    sec_results = str(f"{candid_name}: {vote_percentage_formatted} ({votes})")
    # Adding a new line after each iteration of the second part of the analysis results. 
    results += '\n'
    # Adding the second part of the analysis results to the add-on for the second part. 
    results += sec_results
    # Calculating the winning candidate. 
    if votes > winner_count:
        winner_count = votes
        winner = candid_name
# Writing the third part of the analysis results. 
third_result = str(f"---------------------\n"
                    f"Winner: {winner}\n"
                    f"---------------------")
# Writing the final part of the analysis results which sums up the other three parts including the add-on. 
total_results = str(f"{first_result} \n {results} \n {third_result}")
# Saves the analysis results to a text file. 
output_path = os.path.join('analysis', 'main.txt')
with open (output_path, 'w') as textfile:
        textfile.write(total_results)

   
        

        
    
        




    

    








      

      
    









print(f"{first_result}\n")
print(f"{sec_results}\n")
print(f"{third_result}\n")

print(f"{total_results}\n")


