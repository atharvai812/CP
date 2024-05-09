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
