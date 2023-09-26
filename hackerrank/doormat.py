# Read input values
input_values = input().split()
length = int(input_values[0])
width = int(input_values[1])

# Calculate the center position
center = width // 2

# Print the top part of the pattern
for i in range(1, length // 2 + 1):
    pattern = ".|." * (2 * i - 1)
    print(pattern.center(width, '-'))

# Print the welcome message
print("WELCOME".center(width, '-'))

# Print the bottom part of the pattern in reverse order
for i in range(length // 2, 0, -1):
    pattern = ".|." * (2 * i - 1)
    print(pattern.center(width, '-'))
