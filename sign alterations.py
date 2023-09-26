# Function to find continual homogeneous sign sums
def continual_homogeneous_sign_sums(arr):
    sums = []
    current_sum = 0
    current_sign = None

    for num in arr:
        if current_sign is None:
            current_sign = 1 if num > 0 else -1
            current_sum = num
        elif num * current_sign > 0:
            current_sum += num
        else:
            sums.append(current_sum)
            current_sign = 1 if num > 0 else -1
            current_sum = num

    sums.append(current_sum)  # Add the last sum

    return sums

# Input number of test cases
T = int(input())

for _ in range(T):
    # Input N
    N = int(input())

    # Input the list of N integers
    arr = list(map(int, input().split()))

    # Calculate the continual homogeneous sign sums
    sums = continual_homogeneous_sign_sums(arr)

    # Print the sums for this test case
    print(*sums)
