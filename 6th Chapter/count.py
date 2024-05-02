def generate_table(num):
    t = [0, 2, 5, 13]  # Initial values
    for n in range(4, num + 1):
        t.append(2 * t[n - 1] + t[n - 2] + t[n - 3])
    return t

TABLE = generate_table(1000)

while True:
    line = input()
    if not line:
        break
    print(TABLE[int(line)])
