#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_ = []
    for iterat in range(list_length):
        try:
            list_.append(my_list_1[iterat] / my_list_2[iterat])
        except TypeError:
            print("wrong type")
            list_.append(0)
        except ZeroDivisionError:
            print("division by 0")
            list_.append(0)
        except IndexError:
            print("out of range")
            list_.append(0)
        finally:
            pass
    return list_
