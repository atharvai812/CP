while True:
    A, B = input().split()
    if A == '0' and B == '0':
        break
    # Padding the numbers with leading zeros to make them of equal length
    max_len = max(len(A), len(B))
    A = A.zfill(max_len)
    B = B.zfill(max_len)
    # Convert the numbers from strings to lists of integers
    A = [int(digit) for digit in A]
    B = [int(digit) for digit in B]
    carry = 0
    count = 0
    for i in range(max_len - 1, -1, -1):
        carry += A[i] + B[i]
        if carry >= 10:
            count += 1
            carry = 1  # Reset carry to 1 for the next iteration
        else:
            carry = 0
    if count == 0:
        print("No carry operation.")
    else:
        print(f"{count} carry operation{'s' if count > 1 else ''}.")

#Sample Input
#123 456
#555 555
#123 594
#0 0

#Sample Output
#No carry operation.
#3 carry operations.
#1 carry operation