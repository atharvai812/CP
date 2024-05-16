from math import floor, sqrt

def solve(x, y):
    # Calculate the number of steps required
    return floor(sqrt(y - x - 1) + sqrt(y - x + 1))

def main():
    cases = int(input("Enter the number of cases: "))
    results = []
    for _ in range(cases):
        x, y = map(int, input().split())
        results.append(solve(x, y))
    return results

if __name__ == "__main__":
    results = main()
    for result in results:
        print(result)


#Output :
#Enter the number of cases: 3
#45 48
#45 49
#45 50
#3
#3
#4 