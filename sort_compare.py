import time
import random

def insertion_sort(a_list):
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
    while position > 0 and a_list[position - 1] > current_value:
        a_list[position] = a_list[position - 1]
        position = position - 1
    a_list[position] = current_value
    return time.time() - start_time


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    start_time = time.time()
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

    sublist_count = sublist_count // 2

    return time.time() - start_time

def python_sort(a_list):
    start_time = time.time()
    a_list.sort()
    return time.time() - start_time


if __name__ == "__main__":
    list1	= []
    list2       = []
    list3       = []
    list1	= random.sample(xrange(500), 500)
    list2	= random.sample(xrange(1000), 1000)
    list3	= random.sample(xrange(10000), 10000)
    print "Insertion Sort took  %10.7f seconds to run on average" % (sum(((insertion_sort(list1), insertion_sort(list2), insertion_sort(list3))))/3)
    print "Python Sort took %10.7f seconds to run on average" % (sum(((python_sort(list1), python_sort(list2), python_sort(list3))))/3)
    print "Shell Sort took %10.7f seconds to run on average" % (sum(((shell_sort(list1), shell_sort(list2), shell_sort(list3))))/3)

