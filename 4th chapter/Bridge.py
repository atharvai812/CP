def min_crossing_time(n, crossing_times):
    """Find the minimum crossing time for all people."""
    if n == 1:
        return crossing_times[0]
    elif n == 2:
        return max(crossing_times)
    elif n == 3:
        return sum(crossing_times)
    else:
        # Sort the crossing times
        crossing_times.sort()
        total_time = 0
        while n > 3:
            # Strategy: Send the two slowest people first, then send the fastest back,
            # and finally send the two slowest again
            total_time += min(crossing_times[0] + 2 * crossing_times[1] + crossing_times[-1],
                              crossing_times[0] + crossing_times[-2] + 2 * crossing_times[-1])
            n -= 2
        if n == 3:
            total_time += sum(crossing_times)
        else:
            total_time += crossing_times[-1]  # Only one or two people left
        return total_time

# Read input until EOF
cases = int(input())
input()  # Skip the blank line
for _ in range(cases):
    n = int(input())
    crossing_times = [int(input()) for _ in range(n)]
    total_time = min_crossing_time(n, crossing_times)
    print(total_time)
    if n == 1:
        print(crossing_times[0])
    elif n == 2:
        print(*crossing_times)
    elif n == 3:
        print(*crossing_times)
    else:
        # Sort the crossing times
        crossing_times.sort()
        while n > 3:
            # Strategy: Send the two slowest people first, then send the fastest back,
            # and finally send the two slowest again
            print(crossing_times[0], crossing_times[1])
            print(crossing_times[0])
            print(crossing_times[-2], crossing_times[-1])
            print()
            n -= 2
        if n == 3:
            print(*crossing_times)
        else:
            print(crossing_times[-1])
    if _ < cases - 1:
        print()
