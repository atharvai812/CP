
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

#Sample Input
#2
#14
#3
#3
#4
#8
#100
#4
#12
#15
#25
#40


#Sample Output
#5
#15    