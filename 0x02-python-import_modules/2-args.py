#!/usr/bin/python3
def arg():
    my_arguments = ['Hello', 'Welcome', 'To', 'The', 'Best', 'Schoool']
    print(f"{len(my_arguments)} arguments: ")
    for count,  i in enumerate(my_arguments, 1):
        print(f"{count}: {i}")
arg()
