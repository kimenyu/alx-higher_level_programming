#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new = my_list.copy()
    my_list[idx] = element
    if idx < 0 or idx >= len(my_list):
        return new
    else:
        return my_list
