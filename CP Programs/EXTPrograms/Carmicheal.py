def is_prime(n): 
    """Check if a number is prime.""" 
    if n <= 1: 
        return False 
    if n <= 3: 
        return True 
    if n % 2 == 0 or n % 3 == 0: 
        return False 
    i = 5 
    while i * i <= n: 
        if n % i == 0 or n % (i + 2) == 0: 
            return False 
        i += 6 
    return True 
 
def gcd(a, b): 
    """Compute the greatest common divisor of a and b.""" 
    while b: 
        a, b = b, a % b 
    return a 
 
def is_carmichael(n): 
    """Check if a number is a Carmichael number.""" 
    if is_prime(n): 
        return False 
    for a in range(2, n): 
        if gcd(a, n) == 1: 
            if pow(a, n-1, n) != 1: 
                return False 
    return True 
def main(): 
    while True: 
        n = int(input("Enter a number (0 to stop): ")) 
        if n == 0: 
            break 
        if is_carmichael(n): 
            print(f"The number {n} is a Carmichael number.") 
        else: 
            print(f"{n} is normal.") 
if __name__ == "__main__": 
    main() 
    
# Sample Input  
# 1729 
#  17 
#  561 
#  1109 
#  431  
# 0 

#  Sample Output 
#  The number 1729 is a Carmichael number. 
#  17 is normal. 
#  The number 561 is a Carmichael number.  
# 1109 is normal. 
#  431 is normal. 