import math 
 
def find_position(n): 
    root = math.ceil(math.sqrt(n)) 
    next_square = root * root 
 
    if next_square % 2 == 1:  # when nextSquare is odd 
        if next_square - n < root: 
            x = next_square - n + 1 
            y = root 
        else: 
            x = root 
            y = n - (root - 1) * (root - 1) 
    else:  # when nextSquare is even 
        if next_square - n < root: 
            x = root 
            y = next_square - n + 1 
        else: 
            x = n - (root - 1) * (root - 1) 
            y = root 
 
    return x, y 
 
def main(): 
    while True: 
        n = int(input("Enter a number (0 to stop): ")) 
        if n == 0: 
            break 
        x, y = find_position(n) 
        print(f"{x} {y}") 
 
if __name__ == "__main__": 
    main() 
    
# Sample Input 
#  8 
#  20  
# 25  
# 0  
# Sample Output 
#  2 3 
#  5 4 
#  1 5