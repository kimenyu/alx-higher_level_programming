#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    id idx < 0  or idx >= len(my_list):
        return list(my_list)
    else:
        my_list[idx] = element
        return my_list
