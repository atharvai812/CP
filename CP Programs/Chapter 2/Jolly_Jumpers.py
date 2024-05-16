

while True:
	try:
		a = list(map(int, input().split()))
	except EOFError:
		break
		
	n = [0 for i in range(3001)]
	
	for i in range(2, len(a)):
		m = abs(a[i] - a[i-1])
		if n[m] == 0 and m > 0 and m < a[0]:
			n[m] = 1
		
	if sum(n) == a[0] - 1:
		print("Jolly")
	else:
		print("Not jolly")



while True:
	try:
		a = list(map(int, input().split()))
	except EOFError:
		break
		
	n = [0 for i in range(3001)]
	
	for i in range(2, len(a)):
		m = abs(a[i] - a[i-1])
		if n[m] == 0 and m > 0 and m < a[0]:
			n[m] = 1
		
	if sum(n) == a[0] - 1:
		print("Jolly")
	else:
		print("Not jolly")

#Sample Input
#4 1 4 2 3
#5 1 4 2 -1 6

#Sample Output
#Jolly
#Not jolly       		