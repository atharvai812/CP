t = int(input())
for _ in range(t):
    n = int(input())
    input()  # Ignore newline
    original = []
    expected = []
    for i in range(2 * n):
        line = input()
        if i < n:
            original.append(line)
        else:
            expected.append(line)
    
    i = n - 1
    j = n - 1
    while i >= 0:
        if original[i] == expected[j]:
            j -= 1
        i -= 1
    
    while j >= 0:
        print(expected[j])
        j -= 1
    
    print()


#Sample Input
#2
#3
#Yertle
#Duke of Earl
#Sir Lancelot
#Duke of Earl
#Yertle
#Sir Lancelot
#9
#Yertle
#Duke of Earl
#Sir Lancelot
#Elizabeth Windsor
#Michael Eisner
#Richard M. Nixon
#Mr. Rogers
#Ford Perfect
#Mack
#Yertle
#Richard M. Nixon
#Sir Lancelot
#Duke of Earl
#Elizabeth Windsor
#Michael Eisner
#Mr. Rogers
#Ford Perfect
#Mack


#Sample Output
#Duke of Earl
#Sir Lancelot
#Richard M. Nixon
#Yertle