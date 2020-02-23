import os #Import allows you to access code from another module. 'os' means Miscellaneous operating system interfaces
import csv  #csc format is the most common import and export format 

#Creating an object out of the CSV file
budget_data = os.path.join("budget_data.csv") #the file path for "budget_data.csv file" so python can use it in its "open function"

total_months = 0 #The "=" is also know as the "assingment sign". It is nessacary to assign this value to "0" bc later, a counter will be created in order to get "total months"
total_p = 0 #Will be used later in our 'open' command and 'print' command. Same reasons as above. 
value = 0 #same
change = 0 #same
dates = [] #This will create a function for "dates"
profits = [] #This will create a function for "profits"
#Opening and reading the CSV file
with open(budget_data,newline = '') as f: #With statement allows for better syntax and exceptions handling. As well it closes the file automatically
    #open allows us to open the object we created above; "budget_data is our file" and
    #newline = '' means when reading input from the file, if newline is none, univiersal newlines mode is enabled.
    #as f means the variable "f" is being assigned as the csv file
    reader = csv.reader(f, delimiter = ",") #csv reader command allows for 'reader' to open folder 
    #f is the file name, delimiter means a sequence of one or more characters used to specify the boundary between separate, independent regions in plain text
    
    csv_header = next(reader) 
    #This allows python to skip the data from the first columns 
    #"Next" command grabs the next item in the iterator (like a series of list such as our csv file). We place reader there because reader is our object
    #Reading the first row (so that we track the changes properly)
    first_row = next(reader)
    total_months += 1
    total_p += int(first_row[1])
    value = int(first_row[1])
    
    #Going through each row of data after the header & first row 
    for row in reader:
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_p = total_p + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_p)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
with open("budget_output.txt","w") as p:
    p.write('Financial Analysis')
    p.write('\n----------------------------')
    p.write('\nTotal Months: '+str(total_months))
    # Output to text file
    p.write('\nAverage  Change: $'+str(round(avg_change,2)))
    # Output to text file
    p.write('\nGreatest Increase in Profits:  ($'+str(greatest_increase)+')')
    # Output to text file
    p.write('\nGreatest Decrease in Profits:  ($'+str(greatest_decrease)+')')
with open("text.txt","w") as t:

    t.write("hi bye see ya")
 



#Material Recite
#https://stackoverflow.com/questions/19080190/what-does-the-as-command-do-in-python-3-x
#https://docs.python.org/3/library/functions.html#open-newline-parameter
#https://pythonconquerstheuniverse.wordpress.com/2011/05/08/newline-conversion-in-python-3/
#https://data-flair.training/blogs/python-variable-scope/#https://docs.python.org/3/library/csv.html
