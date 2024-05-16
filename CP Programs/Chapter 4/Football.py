class Team:
    def __init__(self, name):
        self.name = name
        self.gplayed = 0
        self.wins = 0
        self.ties = 0
        self.loses = 0
        self.gscored = 0
        self.gagainst = 0
        self.points = 0
        self.games = 0
        self.gd = 0

t = int(input())
for _ in range(t):
    tname = input().strip()
    n = int(input())
    teamMap = {}
    for _ in range(n):
        pname = input().strip()
        teamMap[pname] = Team(pname)
    g = int(input())
    for _ in range(g):
        line = input().strip().split('#')
        pname, scores, pname2 = line[0], line[1].split('@'), line[2]
        a, b = map(int, scores)
        teamMap[pname].gscored += a
        teamMap[pname].gagainst += b
        teamMap[pname2].gscored += b
        teamMap[pname2].gagainst += a
        if a == b:
            teamMap[pname].ties += 1
            teamMap[pname2].ties += 1
        elif a > b:
            teamMap[pname].wins += 1
            teamMap[pname2].loses += 1
        else:
            teamMap[pname].loses += 1
            teamMap[pname2].wins += 1
    res = sorted(teamMap.values(), key=lambda x: (-x.points, -x.wins, -x.gd, -x.gscored, x.games, x.name.lower()))
    print(tname)
    i = 1
    for team in res:
        print(f"{i}) {team.name} {team.points}p, {team.games}g ({team.wins}-{team.ties}-{team.loses}), {team.gd}gd ({team.gscored}-{team.gagainst})")
        i += 1
    if _ < t - 1:
        print()


#Sample Input
#2
#World Cup 1998 - Group A
#4
#Brazil
#Norway
#Morocco
#Scotland
#6
#Brazil#2@1#Scotland
#Norway#2@2#Morocco
#Scotland#1@1#Norway
#Brazil#3@0#Morocco
#Morocco#3@0#Scotland
#Brazil#1@2#Norway
#Some strange tournament
#5
#Team A
#Team B
#Team C
#Team D
#Team E
#5
#Team A#1@1#Team B
#Team A#2@2#Team C
#Team A#0@0#Team D
#Team E#2@1#Team C
#Team E#1@2#Team D


#Sample Output
#World Cup 1998 - Group A
#1) Brazil 6p, 3g (2-0-1), 3gd (6-3)
#2) Norway 5p, 3g (1-2-0), 1gd (5-4)
#3) Morocco 4p, 3g (1-1-1), 0gd (5-5)
#4) Scotland 1p, 3g (0-1-2), -4gd (2-6)
#Some strange tournament
#1) Team D 4p, 2g (1-1-0), 1gd (2-1