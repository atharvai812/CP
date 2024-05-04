def flip(stack, i):
    return stack[:i+1][::-1] + stack[i+1:]

def pancake_sort(stack):
    n = len(stack)
    flips = []
    # Iterate through the stack from the bottom
    for i in range(n - 1, 0, -1):
        # Find the index of the maximum element in the unsorted portion
        max_index = stack.index(max(stack[:i + 1]))
        # If the maximum element is not at the bottom, perform a flip
        if max_index != i:
            # Flip the sub-stack to bring the maximum element to the top
            stack = flip(stack, max_index)
            flips.append(max_index + 1)
            # Flip the whole stack to move the maximum element to the bottom
            stack = flip(stack, i)
            flips.append(i + 1)
    return flips

def main():
    while True:
        try:
            stack = list(map(int, input().split()))
            print(' '.join(map(str, stack)))
            flips = pancake_sort(stack)
            print(' '.join(map(str, flips)) + ' 0')
        except EOFError:
            break

if __name__ == "__main__":
    main()
