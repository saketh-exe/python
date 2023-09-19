def custom_swapcase(input_string):
    result = ""
    for char in input_string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char  # Keep non-alphabetical characters unchanged
    return result

# Test the custom_swapcase function
input_string = input()
swapped_string = custom_swapcase(input_string)
print(swapped_string)  # Output: "hELLO wORLD!"
