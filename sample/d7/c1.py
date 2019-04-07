import collections


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

    ordered_dict = collections.OrderedDict(sorted(loaded_dict.items()))
    searching = True
    order = ""
    while searching:
        searching = False
        for k, v in ordered_dict.items():
            if len(v) == 0:
                order += k
                ordered_dict.pop(k)
                for k2, v2 in ordered_dict.items():
                    if k in v2:
                        ordered_dict[k2] = str(v2).replace(k, "")
                searching = True
                break

    print("The optimal order is : " + order)


if __name__ == '__main__':
    main()
