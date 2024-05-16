adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def drawRectangle(x1, y1, x2, y2, colour):
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            currentImage[i][j] = colour

def isValid(x, y):
    return 0 <= y < len(currentImage) and 0 <= x < len(currentImage[y])

def drawRegion(x, y):
    visited[y][x] = True
    currentImage[y][x] = colour

    for dx, dy in adj:
        x1, y1 = x + dx, y + dy
        if isValid(x1, y1) and not visited[y1][x1] and selectedColour == currentImage[y1][x1]:
            drawRegion(x1, y1)

while True:
    try:
        line = input()
    except EOFError:
        break

    if line == 'X':
        break

    command, *args = line.split()

    if command == 'I':
        m, n = map(int, args)
        visited = [[False] * m for _ in range(n)]
        currentImage = [['O'] * m for _ in range(n)]

    elif command == 'C':
        currentImage = [['O'] * len(currentImage[0]) for _ in range(len(currentImage))]

    elif command == 'L':
        x, y, colour = map(str, args)
        currentImage[int(y) - 1][int(x) - 1] = colour

    elif command == 'V':
        x, y, y1, colour = map(int, args)
        if y > y1:
            y, y1 = y1, y
        drawRectangle(x - 1, y - 1, x - 1, y1 - 1, colour)

    elif command == 'H':
        x, x1, y, colour = map(int, args)
        if x > x1:
            x, x1 = x1, x
        drawRectangle(x - 1, y - 1, x1 - 1, y - 1, colour)

    elif command == 'K':
        x, y, x1, y1, colour = map(int, args)
        if x > x1:
            x, x1 = x1, x
        if y > y1:
            y, y1 = y1, y
        drawRectangle(x - 1, y - 1, x1 - 1, y1 - 1, colour)

    elif command == 'F':
        x, y, colour = map(int, args)
        selectedColour = currentImage[y - 1][x - 1]
        visited = [[False] * len(currentImage[0]) for _ in range(len(currentImage))]
        drawRegion(x - 1, y - 1)

    elif command == 'S':
        name = args[0]
        print(name)
        for row in currentImage:
            print(''.join(row))


adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def drawRectangle(x1, y1, x2, y2, colour):
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            currentImage[i][j] = colour

def isValid(x, y):
    return 0 <= y < len(currentImage) and 0 <= x < len(currentImage[y])

def drawRegion(x, y):
    visited[y][x] = True
    currentImage[y][x] = colour

    for dx, dy in adj:
        x1, y1 = x + dx, y + dy
        if isValid(x1, y1) and not visited[y1][x1] and selectedColour == currentImage[y1][x1]:
            drawRegion(x1, y1)

while True:
    try:
        line = input()
    except EOFError:
        break

    if line == 'X':
        break

    command, *args = line.split()

    if command == 'I':
        m, n = map(int, args)
        visited = [[False] * m for _ in range(n)]
        currentImage = [['O'] * m for _ in range(n)]

    elif command == 'C':
        currentImage = [['O'] * len(currentImage[0]) for _ in range(len(currentImage))]

    elif command == 'L':
        x, y, colour = map(str, args)
        currentImage[int(y) - 1][int(x) - 1] = colour

    elif command == 'V':
        x, y, y1, colour = map(int, args)
        if y > y1:
            y, y1 = y1, y
        drawRectangle(x - 1, y - 1, x - 1, y1 - 1, colour)

    elif command == 'H':
        x, x1, y, colour = map(int, args)
        if x > x1:
            x, x1 = x1, x
        drawRectangle(x - 1, y - 1, x1 - 1, y - 1, colour)

    elif command == 'K':
        x, y, x1, y1, colour = map(int, args)
        if x > x1:
            x, x1 = x1, x
        if y > y1:
            y, y1 = y1, y
        drawRectangle(x - 1, y - 1, x1 - 1, y1 - 1, colour)

    elif command == 'F':
        x, y, colour = map(int, args)
        selectedColour = currentImage[y - 1][x - 1]
        visited = [[False] * len(currentImage[0]) for _ in range(len(currentImage))]
        drawRegion(x - 1, y - 1)

    elif command == 'S':
        name = args[0]
        print(name)
        for row in currentImage:
            print(''.join(row))


#Sample Input
#I 5 6
#L 2 3 A
#S one.bmp
#G 2 3 J
#F 3 3 J
#V 2 3 4 W
#H 3 4 2 Z
#S two.bmp
#X

#Sample Output
#one.bmp
#OOOOO
#OOOOO
#OAOOO
#OOOOO
#OOOOO
#OOOOO
#two.bmp
#JJJJJ
#JJZZJ
#JWJJJ
#JWJJJ
#JJJJJ
#JJJJJ