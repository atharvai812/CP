import sys

def cbin(n,k):
	if k > n//2:
		k = n - k
		
	top = 1
	bot = 1
	for i in range(2,k+1):
		bot *= i
	for i in range(n-k+1,n+1):
		top *= i
	return top//bot
	
lines = iter(sys.stdin.read().splitlines())

T = int(next(lines))

for line in lines:
	row = int(line)
	col = min(row,5)
	cont = 0
	for j in range(col):
		cont += cbin(row-1,j)
	
	if cont == 0:
		cont += 1

	print(cont,sep = "", end = "\n")