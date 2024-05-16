def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    iterations = 0
    while not is_palindrome(n):
        reversed_n = int(str(n)[::-1])
        n += reversed_n
        iterations += 1
    return iterations, n

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        number = int(input())
        iterations, palindrome = reverse_and_add(number)
        print(iterations, palindrome)

if __name__ == "__main__":
    main()


#Sample Input
#195
#265
#750

#Sample Output
#4 9339
#5 45254
#3 6666