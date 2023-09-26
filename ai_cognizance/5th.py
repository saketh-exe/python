import pandas as pd
import matplotlib.pyplot as plt

# Generate data
sizeh = list(range(700, 2410, 10))  # Range from 700 to 2400, multiples of 10
prices = [10 * x ** 2 + 2 * x for x in sizeh]  # Calculate prices using the equation

# Create a DataFrame
data = pd.DataFrame({'Size(sq feet)': sizeh, 'Price': prices})

# Save data to a CSV file
data.to_csv('house_prices.csv', index=False)

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(sizeh, prices, marker='o', linestyle='-')
plt.title('House Prices vs. Size of Houses')
plt.xlabel('Size of Houses (sq feet)')
plt.ylabel('Price ($)')
plt.grid(True)

# Show or save the plot
plt.tight_layout()
plt.savefig('house_prices.png')  # Save the plot as an image file
plt.show()
