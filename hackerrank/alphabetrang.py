import string

letters = list(string.ascii_lowercase)

def print_rangoli(size):
    output_list = []
    width = (size * 2 - 1) * 2 - 1
    size_letters = letters[:size][::-1]
    
    for i in range(1, len(size_letters) + 1):
        half = "-".join(size_letters[0:i])
        half += half[:-1][::-1]
        output_list.append(half.center(width, "-"))
        
    output_list.extend(output_list[:-1][::-1])
    
    for output in output_list:
        print(output)