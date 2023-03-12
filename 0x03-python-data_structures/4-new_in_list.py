#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list=[]
    new = my_list.copy()
    id idx < 0  or idx >= len(my_list):
        return new
    else:
        my_list[idx] = element
        return my_list
