# Function to find the Stern-Brocot representation of a fraction
def stern_brocot_representation(m, n):
    representation = ""
    while m != 1 or n != 1:
        if m < n:
            representation += "L"
            n -= m
        else:
            representation += "R"
            m -= n
    return representation

# Function to read input and process test cases
def process_test_cases():
    while True:
        try:
            m, n = map(int, input("Enter m and n separated by a space (or enter '1 1' to exit): ").split())
            if m == 1 and n == 1:
                break
            representation = stern_brocot_representation(m, n)
            print(representation)
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

# Call the function to process test cases
process_test_cases()

#Sample Input
#5 7
#878 323
#1 1

#Sample Output
#LRRL
#RRLRRLRLLLLRLRRR