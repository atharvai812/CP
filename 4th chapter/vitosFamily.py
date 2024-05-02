# Function to calculate the total distance from Vito's house to all relatives
def calculate_distance(relatives):
    median_index = len(relatives) // 2
    median_street = relatives[median_index]
    
    total_distance = 0
    for relative in relatives:
        total_distance += abs(relative - median_street)
    
    return total_distance

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    # Read the number of relatives and their street numbers
    relatives_info = list(map(int, input().split()))
    num_relatives = relatives_info[0]
    relatives_streets = sorted(relatives_info[1:])
    
    # Calculate and print the total distance
    total_distance = calculate_distance(relatives_streets)
    print(total_distance)




#######------------Accepted---------------#######