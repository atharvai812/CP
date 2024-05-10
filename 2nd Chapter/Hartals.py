
n = int(input())

for _ in range(n):
    d = int(input())
    m = int(input())
    c = [0] * m
    
    for i in range(m):
        c[i] = int(input())
    
    total = 0
    for i in range(1, d+1):
        if i % 7 == 6 or i % 7 == 0:
            continue
        
        for j in range(m):
            if i % c[j] == 0:
                total += 1
                break
        
    print(total)