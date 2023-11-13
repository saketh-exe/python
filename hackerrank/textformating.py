def print_formatted(number):
    # Calculate the width needed for formatting based on the binary representation of the number
    width = len(bin(number)) - 2

    # Iterate from 1 to number and print the values in the required format
    for i in range(1, number + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        
        # Print the values in the specified format
        print(f"{decimal} {octal} {hexadecimal} {binary}")

# Example usage with the given sample input
number = 17
print_formatted(number)
