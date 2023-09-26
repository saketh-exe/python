import re
import csv

# Initialize an empty list to store numeric values and units
lst = []

# Open and read the file
with open("1.txt", "r") as fh:
    read = fh.read()

# Define the regular expression pattern to match numeric values and units
patt = r'(\d+\.\d+|\d+|[A-Za-z]+)'  # Matches float, int, or string

# Find all matches in the text
matches = re.findall(patt, read)

# Process each match
for a in matches:
    if "." in a:
        num = float(a)
    elif a.isdigit():  # Check if the string consists of digits only
        num = int(a)
    else:
        num = str(a)

    lst.append(num)  

# Create a list of rows, where each row contains four values
rows = [lst[i:i + 4] for i in range(0, len(lst), 4)]

# Open a CSV file for writing
with open("output.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # Write each row of data to the CSV file
    for r in rows:  # Loop through the list of rows
        writer.writerow(r)
