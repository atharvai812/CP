def find_golomb_count(n):
    # Initialize memoization dictionary with the base case
    memo = {1: 1}
    # Iterate from 2 to n to compute Golomb sequence terms iteratively
    for i in range(2, n + 1):
        # Compute the next term in the Golomb sequence using the formula:
        # G(n) = 1 + G(n - G(G(n - 1)))
        memo[i] = 1 + memo[i - memo[memo[i - 1]]]
    # Return the nth term of the Golomb sequence
    return memo[n]

try:
    # Take input from the user
    n = int(input())
    # Validate input
    if n <= 0:
        raise ValueError
except ValueError:
    # Handle invalid input
    print("Invalid input! Please enter a positive integer.")
else:
    # Compute and print the nth term of the Golomb sequence
    print(find_golomb_count(n))

#"INPUT"
#1
#3
#769
#18433

#"OUTPUT"
# 21
#356
#1684
#438744