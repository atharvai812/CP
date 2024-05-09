def comp(j1, j2):
    return j1['time'] * j2['fine'] < j2['time'] * j1['fine']

T = int(input())
for _ in range(T):
    N = int(input())
    jobs = [{'time': 0, 'fine': 0, 'id': 0} for _ in range(N)]
    for i in range(N):
        time, fine = map(int, input().split())
        jobs[i]['time'] = time
        jobs[i]['fine'] = fine
        jobs[i]['id'] = i + 1
    
    jobs.sort(key=comp)

    print(jobs[0]['id'], end='')
    for i in range(1, N):
        print(" ", jobs[i]['id'], end='')
    print()
    
    if T > 1:
        print()
