#CODE INSPIRED BY STUDENT AND TA

from datetime import date
from email.policy import default
import os
import csv


budget_bank = os.path.join('..','Resources', 'budget_data.csv')

with open(budget_bank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"csv_header: {csv_header}")

    total_months = 0
    net_amount = 0
    changes = []
    Avg = []
    g_increase = str
    g_decrease = str
    numbers = []
    new_changes = []
    date_list = []
    pl_list = []
    max_amt = str
    min_amt = str

   
    #find total months
    for row in csvreader:
        total_months += 1
        date_list.append(row[0])

        #find net total amount of profits/loss
        net_amount = net_amount + int(row[1])

        #put numbers of profit/loss in a list to find avg change
        numbers.append(int(row[1]))
        

     
     
      
    print(date_list)    
    print(numbers)   

for i in range(1,len(numbers)):
    changes =  numbers[i] - numbers[i-1]
    pl_list.append(changes)


    
        


      
print(pl_list)

Avg = sum(pl_list)/len(pl_list)      
    
    

#print(pl_list.index(max(pl_list)))
#print(pl_list.index(min(pl_list)))
g_increase = (date_list[pl_list.index(max(pl_list))+1])

g_decrease = (date_list[pl_list.index(min(pl_list))+1])


max_amt = max(pl_list)
min_amt = min(pl_list)


#create .txt file
with open('Analysis.txt', 'w') as txt:
    print("Financial Analysis")

    txt.write("Financial Analysis")
    txt.write("---------------------")

    txt.write(f" Total Months: {len(date_list)}")        
    txt.write(f" Total: $ {net_amount}")
    txt.write(f" Average: $ {Avg}")
    txt.write(f" Greatest Increase: {g_increase}, ($ {max_amt})")
    txt.write(f" Greatest Decrease: {g_decrease}, ($ {min_amt})")
        
        


    
    
        
       
        
        



    
        
        
        

        
        
    

        
        



