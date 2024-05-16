def flip(stack, i):
    """Perform a flip on the stack at position i."""
    return stack[:i][::-1] + stack[i:]

def pancake_sort(stack):
    """Sort the stack of pancakes."""
    flips = []
    n = len(stack)
    for size in range(n, 1, -1):
        max_index = stack.index(size)
        if max_index != size - 1:
            if max_index != 0:
                stack = flip(stack, max_index + 1)
                flips.append(max_index + 1)
            stack = flip(stack, size)
            flips.append(size)
    return flips

# Read input until EOF
while True:
    try:
        stack = list(map(int, input().split()))
        print(*stack)
        flips = pancake_sort(stack)
        print(*flips, 0)
    except EOFError:
        break

#Sample Input
#1 2 3 4 5
#5 4 3 2 1
#5 1 2 3 4


#Sample Output
#1 2 3 4 5
#0
#5 4 3 2 1
#1 0
#5 1 2 3 4
#1 2 0