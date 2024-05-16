import sys

def main():
    T = int(input())
    
    ending_seperator = ""
    
    for _ in range(T):
        n = int(input())
        
        names = []
        eliminated = [False] * n
        
        for _ in range(n):
            names.append(input())
            
        sys.stdin.readline()
        
        ratings = []
        
        temp = input().strip()
        
        while temp != "":
            order = list(map(int, temp.split()))
            order = [x - 1 for x in order]
            ratings.append(order)
            
            if sys.stdin.eof():
                break
                
            temp = input().strip()
        
        num_ratings = len(ratings)
        pos_in_ratings = [0] * num_ratings
        
        winner = -1
        
        count = [0] * n
        
        for i in range(num_ratings):
            count[ratings[i][0]] += 1
        
        while winner == -1:
            for i in range(num_ratings):
                changed = False
                while eliminated[ratings[i][pos_in_ratings[i]]]:
                    pos_in_ratings[i] += 1
                    changed = True
                
                if changed:
                    count[ratings[i][pos_in_ratings[i]]] += 1
            
            highest = max(count)
            lowest = min(count)
            
            if highest == lowest or highest * 2 > num_ratings:
                winner = highest
            else:
                for i in range(n):
                    if count[i] == lowest:
                        eliminated[i] = True
        
        print(ending_seperator, end="")
        ending_seperator = "\n"
        
        for i in range(n):
            if count[i] == winner and not eliminated[i]:
                print(names[i])

if __name__ == "__main__":
    main()

#Sample Input
#1
#3
#John Doe
#Jane Smith
#Sirhan Sirhan
#1 2 3
#2 1 3
#2 3 1
#1 2 3
#3 1 2


#Sample Output
#John Doe