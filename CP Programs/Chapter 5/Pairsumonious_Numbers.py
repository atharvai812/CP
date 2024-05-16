def find_integers(n, sums):
    # Sort the pairwise sums
    sums.sort()
    # Create a dictionary to store the indices of each sum
    indices = {}
    for i, s in enumerate(sums):
        indices.setdefault(s, []).append(i)
    # Initialize variables
    used = 0
    flag = False
    for i in range(2, len(sums)):
        # A[1] + A[2] = sums[i]
        if (sums[0] + sums[1] + sums[i]) % 2 != 0:
            continue
        tmp = (sums[0] + sums[1] + sums[i]) // 2
        A = [0] * n
        A[0] = tmp - sums[i]
        A[1] = tmp - sums[1]
        A[2] = tmp - sums[0]
        used = 1 << i
        idx = 2
        used |= 1
        used |= 2
        for j in range(3, n):
            while used & (1 << idx):
                idx += 1
            A[j] = sums[indices[sums[idx]][0]] - A[0]
            # Delete A[j] + A[0-(j-1)]
            for k in range(j):
                tmp = A[j] + A[k]
                if tmp not in indices:
                    break
                ok = False
                for jt in indices[tmp]:
                    if not (used & (1 << jt)):
                        used |= 1 << jt
                        ok = True
                        break
                if not ok:
                    break
            else:
                continue
            break
        else:
            # Output answer
            flag = True
            result = [str(x) for x in A]
            return " ".join(result)
    if not flag:
        return "Impossible"

def process_test_cases():
    while True:
        try:
            line = input().strip() # Remove leading/trailing whitespace
            if not line:
                break
            # Extract integers from the line
            numbers = [int(x) for x in line.split()]
            n, sums = numbers[0], numbers[1:]
            integers = find_integers(n, sums)
            print(integers)
        except EOFError:
            break

process_test_cases()


#Sample Input
#3 1269 1160 1663
#3 1 1 1
#5 226 223 225 224 227 229 228 226 225 227
#5 216 210 204 212 220 214 222 208 216 210
#5 -1 0 -1 -2 1 0 -1 1 0 -1
#5 79950 79936 79942 79962 79954 79972 79960 79968 79924 79932


#Sample Output
#383 777 886
#Impossible
#11 112 113 114 115
#101 103 107 109 113
#-1 -1 0 0 1
#39953 39971 39979 39983 39989