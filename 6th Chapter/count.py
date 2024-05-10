import sys
	
lines = iter(sys.stdin.read().splitlines())

res = [2,5,13]

for i in range(3,1000):
	res.append(2*res[i-1]+res[i-2]+res[i-3])

for line in lines:

	print(res[int(line)-1],sep = "", end = "\n")