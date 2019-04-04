import datetime
import numpy as np
from datetime import timedelta


def main():
    loaded_dict = {}
    datetime_obj_01011518 = datetime.datetime(1518, 1, 1)
    with open("input.txt") as f:
        for line in f:
            datetime_obj = datetime.datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
            time_diff_1jan_mins = int((datetime_obj - datetime_obj_01011518).total_seconds()/60)
            loaded_dict[time_diff_1jan_mins] = line[19:]

    # could also use OrderDict which would work more often but that's a nice shortcut for this case
    sorted_dict = dict(sorted(loaded_dict.items()))

    slept_time = {}
    current_guard_id = 0
    for k, v in sorted_dict.items():
        # the if else is very restrictive but it is done given the exact input
        if v[0] == "G":
            if current_guard_id != 0:
                try:
                    slept_time[current_guard_id] += sleep_total  # will always be assigned before due to input
                except KeyError:
                    slept_time[current_guard_id] = sleep_total
            sleep_total = 0
            current_guard_id = int(str(v.split("#")[1]).split(" ")[0])
        elif v[0] == "f":
            sleep_start = k
        elif v[0] == "w":
            sleep_total += k - sleep_start  # will always be assigned before due to input

    # the code below could have been done differently but I worked from the basis I had from part 1
    slept_minutes = np.zeros(60, dtype=int)
    slept_minutes_dict = {}
    days_1970_1518 = int((datetime.datetime(1970, 1, 1) - datetime_obj_01011518).days)
    current_guard_id = 0
    for k, v in sorted_dict.items():
        if v[0] == "G":
            for i in range(0, 60):
                if current_guard_id != 0:
                    try:
                        slept_minutes_dict[current_guard_id][i] += slept_minutes[i]
                    except KeyError:
                        slept_minutes_dict[current_guard_id] = np.zeros(60, dtype=int)
                        slept_minutes_dict[current_guard_id][i] = slept_minutes[i]
            current_guard_id = int(str(v.split("#")[1]).split(" ")[0])
            slept_minutes = np.zeros(60, dtype=int)
        elif v[0] == "f":
            sleep_start = k
        elif v[0] == "w":
            start_datetime = datetime.datetime.utcfromtimestamp(sleep_start*60) - timedelta(days=int(days_1970_1518))
            end_datetime = datetime.datetime.utcfromtimestamp(k*60) - timedelta(days=int(days_1970_1518))
            start_minute = start_datetime.minute
            end_minute = end_datetime.minute
            for i in range(start_minute, end_minute):
                slept_minutes[i] += 1

    maximum = 0
    id_sleeper = 0
    for k, v in slept_minutes_dict.items():
        test = max(v)
        if test > maximum:
            id_sleeper = k
            maximum = test
    occurring_minute = np.nonzero(slept_minutes_dict[id_sleeper] == maximum)[0][0]

    print("Solution is: " + str(id_sleeper * occurring_minute))


if __name__ == '__main__':
    main()

