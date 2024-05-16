from datetime import datetime

def parse_time(time_str):
    """Parse time string into datetime object."""
    return datetime.strptime(time_str, "%H:%M")

def calculate_nap_duration(start, end):
    """Calculate duration of a nap."""
    return end - start

# Read input until EOF
case_number = 0
while True:
    try:
        case_number += 1
        n = int(input())
        appointments = []
        for _ in range(n):
            start_str, end_str, appointment = input().split(' ', 2)
            start = parse_time(start_str)
            end = parse_time(end_str)
            appointments.append((start, end))
        
        appointments.sort()  # Sort appointments by start time
        
        max_nap_start = parse_time("10:00")
        max_nap_duration = 0
        
        for i in range(1, n):
            nap_start = appointments[i-1][1]
            nap_end = appointments[i][0]
            nap_duration = calculate_nap_duration(nap_start, nap_end)
            if nap_duration > max_nap_duration:
                max_nap_duration = nap_duration
                max_nap_start = nap_start
        
        nap_end_of_day = parse_time("18:00")
        last_nap_duration = calculate_nap_duration(appointments[-1][1], nap_end_of_day)
        if last_nap_duration > max_nap_duration:
            max_nap_duration = last_nap_duration
            max_nap_start = appointments[-1][1]
        
        hours = max_nap_duration.seconds // 3600
        minutes = (max_nap_duration.seconds % 3600) // 60
        
        print(f"Day #{case_number}: the longest nap starts at {max_nap_start.strftime('%H:%M')} and will last for", end=" ")
        if hours > 0:
            print(f"{hours} hours and", end=" ")
        print(f"{minutes} minutes.")
    
    except EOFError:
        break

#Sample Input
#4
#10:00 12:00 Lectures
#12:00 13:00 Lunch, like always.
#13:00 15:00 Boring lectures...
#15:30 17:45 Reading
#4
#10:00 12:00 Lectures
#12:00 13:00 Lunch, just lunch.
#13:00 15:00 Lectures, lectures... oh, no!
#16:45 17:45 Reading (to be or not to be?)
#4
#10:00 12:00 Lectures, as everyday.
#12:00 13:00 Lunch, again!!!
#13:00 15:00 Lectures, more lectures!
#15:30 17:15 Reading (I love reading, but should I schedule it?)
#1
#12:00 13:00 I love lunch! Have you ever noticed it? :)


#Sample Output
#Day #1: the longest nap starts at 15:00 and will last for 30 minutes.
#Day #2: the longest nap starts at 15:00 and will last for 1 hours and 45 minutes.
#Day #3: the longest nap starts at 17:15 and will last for 45 minutes.
#Day #4: the longest nap starts at 13:00 and will last for 5 hours and 0 minutes.    