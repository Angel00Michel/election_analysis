import csv
import os
from turtle import title

# Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file
with open(file_to_load) as election_data:

    # Print the file object.
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data tot the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file. 
outfile = open(file_to_save, "w")
# Write some data to the file. 
outfile.write("Hello W0RLD")

# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file. 
with open(file_to_save, "w") as txt_file:
    
    # Write some data to the file.
    txt_file.write("Hello W0RLD")

    # Write three counties to the file. 
    txt_file.write("Arapahoe")
    txt_file.write("Denver")
    txt_file.write("Jefferson")

    # Write three counties to the file. [w/ commas]
    txt_file.write("Arapahoe, Denver, Jefferson")

    # Write three counties to the file. [seperate lines]
    txt_file.write("Arapahoe\nDenver\nJefferson")

    # Skill Drill (3.4.3)
    txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")

# Add our dependencies. 
import csv
import os
# Assign a variable to load a file from a path. 
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_load = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)


# Print each row in the CSV file.
    for row in file_reader:
        print(row)

# Question - 3.4.4 --> In the for loop code, {for row in file_reader:}, how would you retrieve the first item from each row?
    for row in file_reader:
        print(row[0])




# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    title = next(file_reader)
    headers = next(file_reader)
    print(headers)
    print(title)


