# 706 - LC-Display

def solve(s, text):
    arr = [ [' - ', '   ', ' - ', ' - ', '   ', ' - ', ' - ', ' - ', ' - ', ' - '],
            ['| |', '  |', '  |', '  |', '| |', '|  ', '|  ', '  |', '| |', '| |'],
            ['   ', '   ', ' - ', ' - ', ' - ', ' - ', ' - ', '   ', ' - ', ' - '],
            ['| |', '  |', '|  ', '  |', '  |', '  |', '| |', '  |', '| |', '  |'],
            [' - ', '   ', ' - ', ' - ', '   ', ' - ', ' - ', '   ', ' - ', ' - ']]

    text_len = len(text)
    for i in range(5):
        row = ''
        for j in range(text_len):
            cell = arr[i][int(text[j])]
            row += '{}{}{}'.format(cell[0], cell[1]*s, cell[2])
            if j != text_len - 1:
                row += ' '
        if i & 1 == 1:
            for _ in range(s):
                print(row)
        else:        
            print(row)

if __name__ == '__main__':
    arr = []
    while True:
        s, n = input().split()
        s = int(s)
        if s == 0:
            break
        arr.append([s, n])
    for i in range(len(arr)):
        solve(arr[i][0], arr[i][1])
        print('')