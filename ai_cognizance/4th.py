import numpy as np

# Specify the file path
file_path = "ai_cognizance/Q4-Dataset.csv"

# Read the data from the file
with open(file_path, 'r') as file:
    # Skip the first line (header)
    next(file)
    
    # Initialize empty lists to store data
    product_ids = []
    prices = []
    ratings = []
    
    # Read each line, split by comma, and remove double quotes
    for line in file:
        parts = line.strip().split(',')
        product_id = parts[0].strip('"')
        price = float(parts[1].strip('"'))
        rating = float(parts[2].strip('"'))
        
        # Append data to lists
        product_ids.append(product_id)
        prices.append(price)
        ratings.append(rating)

# Create a structured array from the lists
dtype = np.dtype([('ProductID', 'U20'), ('price', float), ('rating', float)])
data = np.array(list(zip(product_ids, prices, ratings)), dtype=dtype)

# Sort the array by the 'rating' field
sorted_data = np.sort(data, order='rating')

print("\nSorted Array by Rating:")
print(sorted_data)
