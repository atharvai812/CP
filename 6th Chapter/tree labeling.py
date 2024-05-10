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

def rec(t,b):
	res = 1
	if b > 1:
		dif = t // b
		if dif == 1:
			for i in range(2,b+1):
				res *= i
		else:
			for i in range(b-1):
				res *= cbin(t,dif)
				t -= dif
			res *= pow(rec(dif-1,b),b)
	return res
	
lines = iter(sys.stdin.read().splitlines())

for line in lines:
	b,l = map(int,line.split())
	
	cont = 0
	p = 1
	for i in range(l):
		p *= b
		cont += p

	print(rec(cont,b),sep = "", end = "\n")