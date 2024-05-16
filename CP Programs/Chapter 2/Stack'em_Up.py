import sys

def main():
    s1 = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    s2 = ["Clubs", "Diamonds", "Hearts", "Spades"]

    T = int(input())
    first = True

    for _ in range(T):
        N = int(input())
        p = []
        for _ in range(N):
            p.append(list(map(int, input().split())))
            for j in range(52):
                p[-1][j] -= 1

        cur = list(range(52))

        while True:
            try:
                line = input().strip()
                if not line:
                    break
                K = int(line) - 1
            except EOFError:
                break

            nxt = [0] * 52
            for i in range(52):
                nxt[i] = cur[p[K][i]]
            cur = nxt

        if not first:
            print()
        first = False

        for i in range(52):
            print("{} of {}".format(s1[cur[i] % 13], s2[cur[i] // 13]))

if __name__ == "__main__":
    main()


#Sample Input
#1
#2
#2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
#27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 52 51
#52 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
#27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 1
#1
#2


#Sample Output
#King of Spades
#2 of Clubs
#4 of Clubs
#5 of Clubs
#6 of Clubs
#7 of Clubs
#8 of Clubs
#9 of Clubs
#10 of Clubs
#Jack of Clubs
#Queen of Clubs
#King of Clubs
#Ace of Clubs
#2 of Diamonds
#3 of Diamonds
#4 of Diamonds
#5 of Diamonds
#6 of Diamonds
#7 of Diamonds
#8 of Diamonds
#9 of Diamonds
#10 of Diamonds
#Jack of Diamonds
#Queen of Diamonds
#King of Diamonds
#Ace of Diamonds
#2 of Hearts
#3 of Hearts
#4 of Hearts
#5 of Hearts
#6 of Hearts
#7 of Hearts
#8 of Hearts
#9 of Hearts
#10 of Hearts
#Jack of Hearts
#Queen of Hearts
#King of Hearts
#Ace of Hearts
#2 of Spades
#3 of Spades
#4 of Spades
#5 of Spades
#6 of Spades
#7 of Spades
#8 of Spades
#9 of Spades
#10 of Spades
#Jack of Spades
#Queen of Spades
#Ace of Spades
#3 of Clubs