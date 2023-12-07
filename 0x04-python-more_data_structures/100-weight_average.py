#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_1 = sum(map(lambda a: a[0] * a[1], my_list))
    sum_2 = sum(map(lambda a: a[1], my_list))

    return (sum_1 / sum_2)
