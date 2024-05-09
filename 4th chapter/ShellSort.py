t = int(input())
for _ in range(t):
    n = int(input())
    input()  # Ignore newline
    original = []
    expected = []
    for i in range(2 * n):
        line = input()
        if i < n:
            original.append(line)
        else:
            expected.append(line)
    
    i = n - 1
    j = n - 1
    while i >= 0:
        if original[i] == expected[j]:
            j -= 1
        i -= 1
    
    while j >= 0:
        print(expected[j])
        j -= 1
    
    print()
