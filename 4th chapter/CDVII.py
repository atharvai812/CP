from collections import defaultdict
from datetime import datetime

class Record:
    def __init__(self, month, day, hour, mins, loc, isExit):
        self.month = month
        self.day = day
        self.hour = hour
        self.mins = mins
        self.loc = loc
        self.isExit = isExit
    
    def get_time(self):
        return self.mins + self.hour * 60 + self.day * 24 * 60

def main():
    t = int(input())
    input()  # Ignore blank line
    while t > 0:
        t -= 1
        fares = list(map(int, input().split()))
        license_to_record = defaultdict(list)
        while True:
            try:
                line = input()
                if not line:
                    break
                plate, month, day, hour, mins, command, loc = line.split()
                month, day, hour, mins, loc = map(int, (month, day, hour, mins, loc))
                is_exit = command == 'exit'
                record = Record(month, day, hour, mins, loc, is_exit)
                license_to_record[plate].append(record)
            except EOFError:
                break
        
        for plate, records in license_to_record.items():
            records.sort(key=lambda x: x.get_time())
            total_cents = 200
            for i in range(len(records)):
                if not records[i].isExit and i + 1 < len(records) and records[i+1].isExit:
                    dist = abs(records[i].loc - records[i+1].loc)
                    total_cents += dist * fares[records[i].hour]
                    total_cents += 100
            if total_cents != 200:
                print(f"{plate} ${total_cents/100:.2f}")
        
        if t > 0:
            print()

if __name__ == "__main__":
    main()
