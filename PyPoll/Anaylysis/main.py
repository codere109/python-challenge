#CODE INSPIRED BY STUDENT & TA

import os
import csv
csvpath = os.path.join('..','Resources', 'election_data.csv')



# Initialize the 'Total Vote' count and the 'Winning' count. 
total_votes = 0
winning_count = 0
# Initialize the list of candidates. 
candidates_list = []
# Initialize the dictionary of candidates and their votes. 
candidate_votes = {}



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
        candidate_name = row[2]
        # Incrementing the total vote count for each row in the election data file. 
        total_votes = total_votes + 1
        # Adding a new candidate name to a list for every row in the election data file. 
        if candidate_name not in candidates_list:
            candidates_list.append(candidate_name)
            # Initializing the vote count for each new candidate name. 
            candidate_votes[candidate_name] = 0
        # Adding to the vote count of every candidate name if similar. 
        candidate_votes[candidate_name] += 1
# Writing the first part of the results of the analysis. 
results_1 = str(f"Election Results\n"
                    f"------------------\n"
                    f"Total Votes: {total_votes}\n"
                    f"------------------"
                    )
# Initializing the add-on to the second part of the analysis results. 
all_results_2 = ""
# Initiating a for loop for the 'Candidate Votes' dictionary. 
for candidate_name, votes in candidate_votes.items():
    # Calculating the percentage of votes cast for each candidate. 
    vote_percentage = votes / total_votes
    # Formatting the vote percentage of each candidate to have three decimal places and a percentage sign. 
    vote_percentage_formatted = "{:.3%}".format(vote_percentage)
    # Writing the second part of the analysis results. 
    results_2 = str(f"{candidate_name}: {vote_percentage_formatted} ({votes})")
    # Adding a new line after each iteration of the second part of the analysis results. 
    all_results_2 += '\n'
    # Adding the second part of the analysis results to the add-on for the second part. 
    all_results_2 += results_2
    # Calculating the winning candidate. 
    if votes > winning_count:
        winning_count = votes
        winner = candidate_name
# Writing the third part of the analysis results. 
results_3 = str(f"---------------------\n"
                    f"Winner: {winner}\n"
                    f"---------------------")
# Writing the final part of the analysis results which sums up the other three parts including the add-on. 
total_results = str(f"{results_1} \n {all_results_2} \n {results_3}")
# Saves the analysis results to a text file. 
output_path = os.path.join('analysis', 'main.txt')
with open (output_path, 'w') as textfile:
        textfile.write(total_results)

   
        

        
    
        




    

    








      

      
    









print(f"{results_1}\n")
print(f"{results_2}\n")
print(f"{results_3}\n")

print(f"{total_results}\n")


