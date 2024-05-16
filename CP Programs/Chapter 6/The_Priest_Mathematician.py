T = [0, 1]
opt = 2

for i in range(2, 10001):
    ans = 2 * T[1] + 2**(i - 1) - 1
    for j in range(opt, i):
        cur = 2 * T[j] + 2**(i - j) - 1
        if cur < ans:
            ans = cur
            opt = j
        else:
            break
    T.append(ans)

from sys import stdin

for line in stdin:
    print(T[int(line)])


#"INPUT"
#1
#2
#28
#64

#"OUTPUT"
#1
#3
#769
#18433