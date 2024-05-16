def binomial_coefficient(n, k):
    if k > n // 2:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result *= (n - k + i)
        result //= i
    return result

# Read input from standard input
T = int(input())

# Process each test case
for _ in range(T):
    row = int(input())
    col = min(row, 5)
    total = 0
    # Calculate the total number of ways to choose lines
    for j in range(col):
        total += binomial_coefficient(row - 1, j)
    # If total is 0, increment by 1
    if total == 0:
        total += 1
    # Print the result
    print(total)


#"INPUT"
#4
#1
#2
#3
#4

#"OUTPUT" 
#1
#2
#4
#8
