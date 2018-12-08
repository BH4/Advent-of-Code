"""
The first step I took was to take each event and turn it into a number of
minutes since Jan 1st 1518. This could then be used to sort the events.
This could then be read through in order for both the first and second parts.
"""

import datetime
from collections import defaultdict

event_list = []
ref_date = datetime.datetime(1518, 1, 1)
with open('input/input4.txt') as f:
    # Save each line as an event with the minute number it occurred
    # Note that year doesn't change from 1518

    for line in f:
        line = line.strip()

        event = line.split()

        event_date = datetime.datetime.strptime(event[0]+' '+event[1], '[%Y-%m-%d %H:%M]')
        datedelta = event_date-ref_date
        tot_minute = int(datedelta.total_seconds()/60)

        if event[2] != 'Guard':
            event_list.append((tot_minute, event[2], event_date.minute))
        else:
            # remove # from id
            id_num = int(event[3][1:])
            event_list.append((tot_minute, id_num, event_date.minute))

# sort by the time events happen
event_list.sort()


# add up the total sleep time per id
sleep_time = defaultdict(lambda: defaultdict(int))

curr_id = -1
first_min_asleep = -1
for event in event_list:
    if event[1] == 'falls':
        first_min_asleep = event[2]
    elif event[1] == 'wakes':
        for minute in range(first_min_asleep, event[2]):
            sleep_time[curr_id][minute] += 1
    else:
        curr_id = event[1]

tot_sleep = [(sum(sleep_time[x].values()), x) for x in sleep_time]
best_id = max(tot_sleep)[1]
times_asleep = [(sleep_time[best_id][minute], minute) for minute in sleep_time[best_id]]
best_minute = max(times_asleep)[1]

print(best_id*best_minute)


"""
Change to using the second metric outlined in the problem statement.
"""

best_id = -1
best_minute = -1
most_times = -1
for curr_id in sleep_time:
    for minute in sleep_time[curr_id]:
        times = sleep_time[curr_id][minute]
        if times > most_times:
            best_id = curr_id
            best_minute = minute
            most_times = times

print(best_id*best_minute)
