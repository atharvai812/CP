
def I(line):
    M, N = int(line[1]), int(line[2])
    return [['O']*M for _ in range(N)]

def C(line, arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = 'O'

def L(line, arr):
    X, Y, C = int(line[1]), int(line[2]), line[3]
    arr[Y-1][X-1] = C

def V(line, arr):
    X, Y1, Y2, C = int(line[1]), int(line[2]), int(line[3]), line[4]
    lo, hi = min(Y1, Y2) - 1, max(Y1, Y2)
    for i in range(lo, hi):
        arr[i][X-1] = C

def H(line, arr):
    X1, X2, Y, C = int(line[1]), int(line[2]), int(line[3]), line[4]
    lo, hi = min(X1, X2) - 1, max(X1, X2)
    for i in range(lo, hi):
        arr[Y-1][i] = C

def K(line, arr):
    X1, Y1, X2, Y2, C = int(line[1]), int(line[2]), \
                int(line[3]), int(line[4]), line[5]

    fromX, toX = min(X1, X2) - 1, max(X1, X2)                
    fromY, toY = min(Y1, Y2) - 1, max(Y1, Y2)    
    for i in range(fromY, toY):
        for j in range(fromX, toX):
            arr[i][j] = C

def dfs(line, arr, row, col, old_color, new_color):
    if row < 0 or row >= len(arr):
        return
    if col < 0 or col >= len(arr[0]):
        return

    arr[row][col] = new_color # Color it
    if row > 0 and arr[row-1][col] == old_color: #Up
        dfs(line, arr, row-1, col, old_color, new_color)        
    if row < len(arr) - 1 and arr[row+1][col] == old_color: #Down
        dfs(line, arr, row+1, col, old_color, new_color)
    if col > 0 and arr[row][col - 1] == old_color: #Left
        dfs(line, arr, row, col - 1, old_color, new_color)
    if col < len(arr[0]) -1 and arr[row][col+1] == old_color: #Right
        dfs(line, arr, row, col + 1, old_color, new_color)


def F(line, arr):
    X, Y, new_color = int(line[1]), int(line[2]), line[3]
    old_color = arr[Y-1][X-1]
    if old_color != new_color:
        dfs(line, arr, Y - 1, X - 1, old_color, new_color)

def S(line, arr):
    file = line[1]
    print(file)
    for line in arr:
        print(''.join(line))
# 
def solve(lines):
    arr = None
    for line in lines:
        if len(line) > 0:
            try:
                op = line[0]
                if op == 'I':
                    arr = I(line)
                elif op == 'C':
                    C(line, arr)
                elif op == 'L':
                    L(line, arr)
                elif op == 'V':
                    V(line, arr)
                elif op == 'H':
                    H(line, arr)
                elif op == 'K':
                    K(line, arr)
                elif op == 'F':
                    F(line, arr)
                elif op == 'S':
                    S(line, arr)
                elif op == 'X':
                    break
            except:
                pass

if __name__ == '__main__':
    lines = []
    while True:
        line = input()
        if line == 'X':
            break
        lines.append(line.split())
    solve(lines)
