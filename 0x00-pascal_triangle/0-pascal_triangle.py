#!/usr/bin/python3
'''contains a function pascal_triangle'''


def pascal_triangle(n):
    '''returns a list of lists of integers representing
    the Pascal’s triangle of n'''
    the_list = []
    if n <= 0:
        return the_list
    for listt in range(1, n + 1):
        newlist = [1] * listt
        if listt > 2:
            prevlist = the_list[listt - 2]
            for each in range(listt):
                if each > 0 and each < listt - 1:
                    newlist[each] = prevlist[each - 1] + prevlist[each]
        the_list.append(newlist)
    return the_list
