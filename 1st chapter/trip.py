#1013: The trip

def solve(arr):
    avg = sum(arr)/len(arr)
    pos_diff, neg_diff = 0.0, 0.0
    for num in arr:
        val = int((num - avg) * 100.0) / 100.0
        if val < 0:
            neg_diff += val
        else:
            pos_diff += val
    neg_diff *= -1
    res = neg_diff if neg_diff > pos_diff else pos_diff
    return '${0:.2f}'.format(res)

if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            if N == 0:
                break
            arr = []
            for _ in range(N):
                arr.append(float(input()))
            print(solve(arr))
        except EOFError:
            break        