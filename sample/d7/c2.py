def main():
    loaded_dict = {}
    with open("input.txt") as f:
        for line in f:
            start = line[5]
            end = line[36]
            if start not in loaded_dict:
                loaded_dict[start] = ""
            try:
                loaded_dict[end] += start
            except KeyError:
                loaded_dict[end] = start

    number_of_workers = 6
    availabilities = [("", 0)] * number_of_workers
    searching = True
    time = 0

    while searching:
        searching = False

        # Update the work shifts
        for i in range(0, len(availabilities)):
            if availabilities[i][1] == 1:
                task_done = availabilities[i][0]
                availabilities[i] = ("", 0)
                loaded_dict.pop(task_done)
                for k, v in loaded_dict.items():
                    if task_done in v:
                        loaded_dict[k] = str(v).replace(task_done, "")
                print(loaded_dict)
            elif availabilities[i][1] > 0:
                availabilities[i] = (availabilities[i][0], availabilities[i][1]-1)

        # Assign workers shifts
        for k, v in loaded_dict.items():
            searching = True
            if len(v) == 0:  # check if task can be done

                # check if not already worked on
                open_task = True
                for availability in availabilities:
                    if availability[0] == k:
                        open_task = False

                # check if free worker to work on it and if so assign him to it
                if open_task:
                    for i in range(0, len(availabilities)):
                        if availabilities[i][1] == 0:
                            availabilities[i] = (k, ord(k) - 64 + 60)
                            break
        if loaded_dict:
            time += 1

    print("The total time to finish all the tasks is : " + str(time))


if __name__ == '__main__':
    main()
