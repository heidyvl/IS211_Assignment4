import time
import random
import timeit

def sequential_search (a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found, (time.time() - start_time)


def ordered_sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
    else:
          pos = pos+1
    return found, (time.time() - start_time)


def binary_search_iterative(a_list, item):
    start_time = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
    else:
        first = midpoint + 1
    return found, (time.time() - start_time)

def binary_search_recursive(a_list, item):
    start_time = time.time()
    if len(a_list) == 0:
        return False, start_time
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True, (time.time() - start_time)
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item), (time.time() - start_time)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item),  (time.time() - start_time)

if __name__ == "__main__":
    list1	= []
    list2	= []
    list3	= []
    list4	= []
    list5	= []
    list6	= []
    list7	= []
    list8	= []
    list9	= []
    list10	= []
    list11	= []
    list12	= []
    list13	= []
    list14	= []
    list15	= []
    list16	= []
    list17	= []
    list18	= []
    list19	= []
    list20	= []
    list21	= []
    list22	= []
    list23	= []
    list24	= []
    list25	= []
    list26	= []
    list27	= []
    list28	= []
    list29	= []
    list30	= []
    list31	= []
    list32	= []
    list33	= []
    list34	= []
    list35	= []
    list36	= []
    list37	= []
    list38	= []
    list39	= []
    list40	= []
    list41	= []
    list42	= []
    list43	= []
    list44	= []
    list45	= []
    list46	= []
    list47	= []
    list48	= []
    list49	= []
    list50	= []
    list51	= []
    list52	= []
    list53	= []
    list54	= []
    list55	= []
    list56	= []
    list57	= []
    list58	= []
    list59	= []
    list60	= []
    list61	= []
    list62	= []
    list63	= []
    list64	= []
    list65	= []
    list66	= []
    list67	= []
    list68	= []
    list69	= []
    list70	= []
    list71	= []
    list72	= []
    list73	= []
    list74	= []
    list75	= []
    list76	= []
    list77	= []
    list78	= []
    list79	= []
    list80	= []
    list81	= []
    list82	= []
    list83	= []
    list84	= []
    list85	= []
    list86	= []
    list87	= []
    list88	= []
    list89	= []
    list90	= []
    list91	= []
    list92	= []
    list93	= []
    list94	= []
    list95	= []
    list96	= []
    list97	= []
    list98	= []
    list99	= []
    list100	= []
    list1	= random.sample(xrange(500), 500)
    list2	= random.sample(xrange(500), 500)
    list3	= random.sample(xrange(500), 500)
    list4	= random.sample(xrange(500), 500)
    list5	= random.sample(xrange(500), 500)
    list6	= random.sample(xrange(500), 500)
    list7	= random.sample(xrange(500), 500)
    list8	= random.sample(xrange(500), 500)
    list9	= random.sample(xrange(500), 500)
    list10	= random.sample(xrange(500), 500)
    list11	= random.sample(xrange(500), 500)
    list12	= random.sample(xrange(500), 500)
    list13	= random.sample(xrange(500), 500)
    list14	= random.sample(xrange(500), 500)
    list15	= random.sample(xrange(500), 500)
    list16	= random.sample(xrange(500), 500)
    list17	= random.sample(xrange(500), 500)
    list18	= random.sample(xrange(500), 500)
    list19	= random.sample(xrange(500), 500)
    list20	= random.sample(xrange(500), 500)
    list21	= random.sample(xrange(500), 500)
    list22	= random.sample(xrange(500), 500)
    list23	= random.sample(xrange(500), 500)
    list24	= random.sample(xrange(500), 500)
    list25	= random.sample(xrange(500), 500)
    list26	= random.sample(xrange(500), 500)
    list27	= random.sample(xrange(500), 500)
    list28	= random.sample(xrange(500), 500)
    list29	= random.sample(xrange(500), 500)
    list30	= random.sample(xrange(500), 500)
    list31	= random.sample(xrange(500), 500)
    list32	= random.sample(xrange(500), 500)
    list33	= random.sample(xrange(500), 500)
    list34	= random.sample(xrange(1000), 1000)
    list35	= random.sample(xrange(1000), 1000)
    list36	= random.sample(xrange(1000), 1000)
    list37	= random.sample(xrange(1000), 1000)
    list38	= random.sample(xrange(1000), 1000)
    list39	= random.sample(xrange(1000), 1000)
    list40	= random.sample(xrange(1000), 1000)
    list41	= random.sample(xrange(1000), 1000)
    list42	= random.sample(xrange(1000), 1000)
    list43	= random.sample(xrange(1000), 1000)
    list44	= random.sample(xrange(1000), 1000)
    list45	= random.sample(xrange(1000), 1000)
    list46	= random.sample(xrange(1000), 1000)
    list47	= random.sample(xrange(1000), 1000)
    list48	= random.sample(xrange(1000), 1000)
    list49	= random.sample(xrange(1000), 1000)
    list50	= random.sample(xrange(1000), 1000)
    list51	= random.sample(xrange(1000), 1000)
    list52	= random.sample(xrange(1000), 1000)
    list53	= random.sample(xrange(1000), 1000)
    list54	= random.sample(xrange(1000), 1000)
    list55	= random.sample(xrange(1000), 1000)
    list56	= random.sample(xrange(1000), 1000)
    list57	= random.sample(xrange(1000), 1000)
    list58	= random.sample(xrange(1000), 1000)
    list59	= random.sample(xrange(1000), 1000)
    list60	= random.sample(xrange(1000), 1000)
    list61	= random.sample(xrange(1000), 1000)
    list62	= random.sample(xrange(1000), 1000)
    list63	= random.sample(xrange(1000), 1000)
    list64	= random.sample(xrange(1000), 1000)
    list65	= random.sample(xrange(1000), 1000)
    list66	= random.sample(xrange(1000), 1000)
    list67	= random.sample(xrange(1000), 1000)
    list68	= random.sample(xrange(10000), 10000)
    list69	= random.sample(xrange(10000), 10000)
    list70	= random.sample(xrange(10000), 10000)
    list71	= random.sample(xrange(10000), 10000)
    list72	= random.sample(xrange(10000), 10000)
    list73	= random.sample(xrange(10000), 10000)
    list74	= random.sample(xrange(10000), 10000)
    list75	= random.sample(xrange(10000), 10000)
    list76	= random.sample(xrange(10000), 10000)
    list77	= random.sample(xrange(10000), 10000)
    list78	= random.sample(xrange(10000), 10000)
    list79	= random.sample(xrange(10000), 10000)
    list80	= random.sample(xrange(10000), 10000)
    list81	= random.sample(xrange(10000), 10000)
    list82	= random.sample(xrange(10000), 10000)
    list83	= random.sample(xrange(10000), 10000)
    list84	= random.sample(xrange(10000), 10000)
    list85	= random.sample(xrange(10000), 10000)
    list86	= random.sample(xrange(10000), 10000)
    list87	= random.sample(xrange(10000), 10000)
    list88	= random.sample(xrange(10000), 10000)
    list89	= random.sample(xrange(10000), 10000)
    list90	= random.sample(xrange(10000), 10000)
    list91	= random.sample(xrange(10000), 10000)
    list92	= random.sample(xrange(10000), 10000)
    list93	= random.sample(xrange(10000), 10000)
    list94	= random.sample(xrange(10000), 10000)
    list95	= random.sample(xrange(10000), 10000)
    list96	= random.sample(xrange(10000), 10000)
    list97	= random.sample(xrange(10000), 10000)
    list98	= random.sample(xrange(10000), 10000)
    list99	= random.sample(xrange(10000), 10000)
    list100	= random.sample(xrange(10000), 10000)

    print "Sequential Search took  %10.7f seconds to run on average" % (sum(((sequential_search(sorted(list1), -1))[1], (sequential_search(sorted(list2), -1))[1], (sequential_search(sorted(list3), -1))[1], (sequential_search(sorted(list4), -1))[1],
                             (sequential_search(sorted(list5), -1))[1], (sequential_search(sorted(list6), -1))[1], (sequential_search(sorted(list7), -1))[1],
                             (sequential_search(sorted(list8), -1))[1], (sequential_search(sorted(list9), -1))[1], (sequential_search(sorted(list10), -1))[1], (sequential_search(sorted(list11), -1))[1],
                             (sequential_search(sorted(list12), -1))[1],
                             (sequential_search(sorted(list13), -1))[1], (sequential_search(sorted(list14), -1))[1],(sequential_search(sorted(list15), -1))[1],
                             (sequential_search(sorted(list16), -1))[1], (sequential_search(sorted(list17), -1))[1],
                             (sequential_search(sorted(list18), -1))[1], (sequential_search(sorted(list19), -1))[1], (sequential_search(sorted(list20), -1))[1],
                             (sequential_search(sorted(list21), -1))[1], (sequential_search(sorted(list22), -1))[1], (sequential_search(sorted(list23), -1))[1],
                             (sequential_search(sorted(list24), -1))[1], (sequential_search(sorted(list25), -1))[1], (sequential_search(sorted(list26), -1))[1],
                             (sequential_search(sorted(list27), -1))[1], (sequential_search(sorted(list28), -1))[1], (sequential_search(sorted(list29), -1))[1],
                             (sequential_search(sorted(list30), -1))[1], (sequential_search(sorted(list31), -1))[1], (sequential_search(sorted(list32), -1))[1],
                             (sequential_search(sorted(list33), -1))[1], (sequential_search(sorted(list34), -1))[1], (sequential_search(sorted(list35), -1))[1],
                             (sequential_search(sorted(list36), -1))[1], (sequential_search(sorted(list37), -1))[1], (sequential_search(sorted(list38), -1))[1],
                             (sequential_search(sorted(list39), -1))[1], (sequential_search(sorted(list40), -1))[1], (sequential_search(sorted(list41), -1))[1],
                             (sequential_search(sorted(list42), -1))[1], (sequential_search(sorted(list43), -1))[1], (sequential_search(sorted(list44), -1))[1],
                             (sequential_search(sorted(list45), -1))[1], (sequential_search(sorted(list46), -1))[1], (sequential_search(sorted(list47), -1))[1],
                             (sequential_search(sorted(list48), -1))[1], (sequential_search(sorted(list49), -1))[1], (sequential_search(sorted(list50), -1))[1],
                             (sequential_search(sorted(list51), -1))[1], (sequential_search(sorted(list52), -1))[1], (sequential_search(sorted(list53), -1))[1],
                             (sequential_search(sorted(list54), -1))[1], (sequential_search(sorted(list55), -1))[1], (sequential_search(sorted(list56), -1))[1],
                             (sequential_search(sorted(list57), -1))[1], (sequential_search(sorted(list58), -1))[1], (sequential_search(sorted(list59), -1))[1],
                             (sequential_search(sorted(list60), -1))[1], (sequential_search(sorted(list61), -1))[1], (sequential_search(sorted(list62), -1))[1],
                             (sequential_search(sorted(list63), -1))[1], (sequential_search(sorted(list64), -1))[1], (sequential_search(sorted(list65), -1))[1],
                             (sequential_search(sorted(list66), -1))[1], (sequential_search(sorted(list67), -1))[1], (sequential_search(sorted(list68), -1))[1],
                             (sequential_search(sorted(list69), -1))[1], (sequential_search(sorted(list70), -1))[1], (sequential_search(sorted(list71), -1))[1],
                             (sequential_search(sorted(list72), -1))[1], (sequential_search(sorted(list73), -1))[1], (sequential_search(sorted(list74), -1))[1],
                             (sequential_search(sorted(list75), -1))[1], (sequential_search(sorted(list76), -1))[1], (sequential_search(sorted(list77), -1))[1],
                             (sequential_search(sorted(list78), -1))[1], (sequential_search(sorted(list79), -1))[1], (sequential_search(sorted(list80), -1))[1],
                             (sequential_search(sorted(list81), -1))[1], (sequential_search(sorted(list82), -1))[1], (sequential_search(sorted(list83), -1))[1],
                             (sequential_search(sorted(list84), -1))[1], (sequential_search(sorted(list85), -1))[1], (sequential_search(sorted(list86), -1))[1],
                             (sequential_search(sorted(list87), -1))[1], (sequential_search(sorted(list88), -1))[1], (sequential_search(sorted(list89), -1))[1],
                             (sequential_search(sorted(list90), -1))[1], (sequential_search(sorted(list91), -1))[1], (sequential_search(sorted(list92), -1))[1],
                             (sequential_search(sorted(list93), -1))[1], (sequential_search(sorted(list94), -1))[1], (sequential_search(sorted(list95), -1))[1],
                             (sequential_search(sorted(list96), -1))[1], (sequential_search(sorted(list97), -1))[1], (sequential_search(sorted(list98), -1))[1],
                             (sequential_search(sorted(list99), -1))[1], (sequential_search(sorted(list100), -1))[1]))/100)
              
    

    print "Ordered Sequential Search took  %10.7f seconds to run on average" % (sum(((ordered_sequential_search(sorted(list1), -1))[1], (ordered_sequential_search(sorted(list2), -1))[1], (ordered_sequential_search(sorted(list3), -1))[1], (ordered_sequential_search(sorted(list4), -1))[1],
                             (ordered_sequential_search(sorted(list5), -1))[1],
                             (ordered_sequential_search(sorted(list6), -1))[1], (ordered_sequential_search(sorted(list7), -1))[1],
                             (ordered_sequential_search(sorted(list8), -1))[1], (ordered_sequential_search(sorted(list9), -1))[1],
                             (ordered_sequential_search(sorted(list10), -1))[1], (ordered_sequential_search(sorted(list11), -1))[1],(ordered_sequential_search(sorted(list12), -1))[1],
                             (ordered_sequential_search(sorted(list13), -1))[1], (ordered_sequential_search(sorted(list14), -1))[1],(ordered_sequential_search(sorted(list15), -1))[1],
                             (ordered_sequential_search(sorted(list16), -1))[1], (ordered_sequential_search(sorted(list17), -1))[1],
                             (ordered_sequential_search(sorted(list18), -1))[1], (ordered_sequential_search(sorted(list19), -1))[1], (ordered_sequential_search(sorted(list20), -1))[1],
                             (ordered_sequential_search(sorted(list21), -1))[1], (ordered_sequential_search(sorted(list22), -1))[1], (ordered_sequential_search(sorted(list23), -1))[1],
                             (ordered_sequential_search(sorted(list24), -1))[1], (ordered_sequential_search(sorted(list25), -1))[1], (ordered_sequential_search(sorted(list26), -1))[1],
                             (ordered_sequential_search(sorted(list27), -1))[1], (ordered_sequential_search(sorted(list28), -1))[1], (ordered_sequential_search(sorted(list29), -1))[1],
                             (ordered_sequential_search(sorted(list30), -1))[1], (ordered_sequential_search(sorted(list31), -1))[1], (ordered_sequential_search(sorted(list32), -1))[1],
                             (ordered_sequential_search(sorted(list33), -1))[1], (ordered_sequential_search(sorted(list34), -1))[1], (ordered_sequential_search(sorted(list35), -1))[1],
                             (ordered_sequential_search(sorted(list36), -1))[1], (ordered_sequential_search(sorted(list37), -1))[1], (ordered_sequential_search(sorted(list38), -1))[1],
                             (ordered_sequential_search(sorted(list39), -1))[1], (ordered_sequential_search(sorted(list40), -1))[1], (ordered_sequential_search(sorted(list41), -1))[1],
                             (ordered_sequential_search(sorted(list42), -1))[1], (ordered_sequential_search(sorted(list43), -1))[1], (ordered_sequential_search(sorted(list44), -1))[1],
                             (ordered_sequential_search(sorted(list45), -1))[1], (ordered_sequential_search(sorted(list46), -1))[1], (ordered_sequential_search(sorted(list47), -1))[1],
                             (ordered_sequential_search(sorted(list48), -1))[1], (ordered_sequential_search(sorted(list49), -1))[1], (ordered_sequential_search(sorted(list50), -1))[1],
                             (ordered_sequential_search(sorted(list51), -1))[1], (ordered_sequential_search(sorted(list52), -1))[1], (ordered_sequential_search(sorted(list53), -1))[1],
                             (ordered_sequential_search(sorted(list54), -1))[1], (ordered_sequential_search(sorted(list55), -1))[1], (ordered_sequential_search(sorted(list56), -1))[1],
                             (ordered_sequential_search(sorted(list57), -1))[1], (ordered_sequential_search(sorted(list58), -1))[1], (ordered_sequential_search(sorted(list59), -1))[1],
                             (ordered_sequential_search(sorted(list60), -1))[1], (ordered_sequential_search(sorted(list61), -1))[1], (ordered_sequential_search(sorted(list62), -1))[1],
                             (ordered_sequential_search(sorted(list63), -1))[1], (ordered_sequential_search(sorted(list64), -1))[1], (ordered_sequential_search(sorted(list65), -1))[1],
                             (ordered_sequential_search(sorted(list66), -1))[1], (ordered_sequential_search(sorted(list67), -1))[1], (ordered_sequential_search(sorted(list68), -1))[1],
                             (ordered_sequential_search(sorted(list69), -1))[1], (ordered_sequential_search(sorted(list70), -1))[1], (ordered_sequential_search(sorted(list71), -1))[1],
                             (ordered_sequential_search(sorted(list72), -1))[1], (ordered_sequential_search(sorted(list73), -1))[1], (ordered_sequential_search(sorted(list74), -1))[1],
                             (ordered_sequential_search(sorted(list75), -1))[1], (ordered_sequential_search(sorted(list76), -1))[1], (ordered_sequential_search(sorted(list77), -1))[1],
                             (ordered_sequential_search(sorted(list78), -1))[1], (ordered_sequential_search(sorted(list79), -1))[1], (ordered_sequential_search(sorted(list80), -1))[1],
                             (ordered_sequential_search(sorted(list81), -1))[1], (ordered_sequential_search(sorted(list82), -1))[1], (ordered_sequential_search(sorted(list83), -1))[1],
                             (ordered_sequential_search(sorted(list84), -1))[1], (ordered_sequential_search(sorted(list85), -1))[1], (ordered_sequential_search(sorted(list86), -1))[1],
                             (ordered_sequential_search(sorted(list87), -1))[1], (ordered_sequential_search(sorted(list88), -1))[1], (ordered_sequential_search(sorted(list89), -1))[1],
                             (ordered_sequential_search(sorted(list90), -1))[1], (ordered_sequential_search(sorted(list91), -1))[1], (ordered_sequential_search(sorted(list92), -1))[1],
                             (ordered_sequential_search(sorted(list93), -1))[1], (ordered_sequential_search(sorted(list94), -1))[1], (ordered_sequential_search(sorted(list95), -1))[1],
                             (ordered_sequential_search(sorted(list96), -1))[1], (ordered_sequential_search(sorted(list97), -1))[1], (ordered_sequential_search(sorted(list98), -1))[1],
                             (ordered_sequential_search(sorted(list99), -1))[1], (ordered_sequential_search(sorted(list100), -1))[1]))/100)


    print "Binary Search Iterative took  %10.7f seconds to run on average" % (sum(((binary_search_iterative(sorted(list1), -1))[1], (binary_search_iterative(sorted(list2), -1))[1], (binary_search_iterative(sorted(list3), -1))[1], (binary_search_iterative(sorted(list4), -1))[1],
                             (binary_search_iterative(sorted(list5), -1))[1],
                             (binary_search_iterative(sorted(list6), -1))[1], (binary_search_iterative(sorted(list7), -1))[1],
                             (binary_search_iterative(sorted(list8), -1))[1],  (binary_search_iterative(sorted(list9), -1))[1],
                             (binary_search_iterative(sorted(list10), -1))[1], (binary_search_iterative(sorted(list11), -1))[1],(binary_search_iterative(sorted(list12), -1))[1],
                             (binary_search_iterative(sorted(list13), -1))[1], (binary_search_iterative(sorted(list14), -1))[1],(binary_search_iterative(sorted(list15), -1))[1],
                             (binary_search_iterative(sorted(list16), -1))[1], (binary_search_iterative(sorted(list17), -1))[1],
                             (binary_search_iterative(sorted(list18), -1))[1], (binary_search_iterative(sorted(list19), -1))[1], (binary_search_iterative(sorted(list20), -1))[1],
                             (binary_search_iterative(sorted(list21), -1))[1], (binary_search_iterative(sorted(list22), -1))[1], (binary_search_iterative(sorted(list23), -1))[1],
                             (binary_search_iterative(sorted(list24), -1))[1], (binary_search_iterative(sorted(list25), -1))[1], (binary_search_iterative(sorted(list26), -1))[1],
                             (binary_search_iterative(sorted(list27), -1))[1], (binary_search_iterative(sorted(list28), -1))[1], (binary_search_iterative(sorted(list29), -1))[1],
                             (binary_search_iterative(sorted(list30), -1))[1], (binary_search_iterative(sorted(list31), -1))[1], (binary_search_iterative(sorted(list32), -1))[1],
                             (binary_search_iterative(sorted(list33), -1))[1], (binary_search_iterative(sorted(list34), -1))[1], (binary_search_iterative(sorted(list35), -1))[1],
                             (binary_search_iterative(sorted(list36), -1))[1], (binary_search_iterative(sorted(list37), -1))[1], (binary_search_iterative(sorted(list38), -1))[1],
                             (binary_search_iterative(sorted(list39), -1))[1], (binary_search_iterative(sorted(list40), -1))[1], (binary_search_iterative(sorted(list41), -1))[1],
                             (binary_search_iterative(sorted(list42), -1))[1], (binary_search_iterative(sorted(list43), -1))[1], (binary_search_iterative(sorted(list44), -1))[1],
                             (binary_search_iterative(sorted(list45), -1))[1], (binary_search_iterative(sorted(list46), -1))[1], (binary_search_iterative(sorted(list47), -1))[1],
                             (binary_search_iterative(sorted(list48), -1))[1], (binary_search_iterative(sorted(list49), -1))[1], (binary_search_iterative(sorted(list50), -1))[1],
                             (binary_search_iterative(sorted(list51), -1))[1], (binary_search_iterative(sorted(list52), -1))[1], (binary_search_iterative(sorted(list53), -1))[1],
                             (binary_search_iterative(sorted(list54), -1))[1], (binary_search_iterative(sorted(list55), -1))[1], (binary_search_iterative(sorted(list56), -1))[1],
                             (binary_search_iterative(sorted(list57), -1))[1], (binary_search_iterative(sorted(list58), -1))[1], (binary_search_iterative(sorted(list59), -1))[1],
                             (binary_search_iterative(sorted(list60), -1))[1], (binary_search_iterative(sorted(list61), -1))[1], (binary_search_iterative(sorted(list62), -1))[1],
                             (binary_search_iterative(sorted(list63), -1))[1], (binary_search_iterative(sorted(list64), -1))[1], (binary_search_iterative(sorted(list65), -1))[1],
                             (binary_search_iterative(sorted(list66), -1))[1], (binary_search_iterative(sorted(list67), -1))[1], (binary_search_iterative(sorted(list68), -1))[1],
                             (binary_search_iterative(sorted(list69), -1))[1], (binary_search_iterative(sorted(list70), -1))[1], (binary_search_iterative(sorted(list71), -1))[1],
                             (binary_search_iterative(sorted(list72), -1))[1], (binary_search_iterative(sorted(list73), -1))[1], (binary_search_iterative(sorted(list74), -1))[1],
                             (binary_search_iterative(sorted(list75), -1))[1], (binary_search_iterative(sorted(list76), -1))[1], (binary_search_iterative(sorted(list77), -1))[1],
                             (binary_search_iterative(sorted(list78), -1))[1], (binary_search_iterative(sorted(list79), -1))[1], (binary_search_iterative(sorted(list80), -1))[1],
                             (binary_search_iterative(sorted(list81), -1))[1], (binary_search_iterative(sorted(list82), -1))[1], (binary_search_iterative(sorted(list83), -1))[1],
                             (binary_search_iterative(sorted(list84), -1))[1], (binary_search_iterative(sorted(list85), -1))[1], (binary_search_iterative(sorted(list86), -1))[1],
                             (binary_search_iterative(sorted(list87), -1))[1], (binary_search_iterative(sorted(list88), -1))[1], (binary_search_iterative(sorted(list89), -1))[1],
                             (binary_search_iterative(sorted(list90), -1))[1], (binary_search_iterative(sorted(list91), -1))[1], (binary_search_iterative(sorted(list92), -1))[1],
                             (binary_search_iterative(sorted(list93), -1))[1], (binary_search_iterative(sorted(list94), -1))[1], (binary_search_iterative(sorted(list95), -1))[1],
                             (binary_search_iterative(sorted(list96), -1))[1], (binary_search_iterative(sorted(list97), -1))[1], (binary_search_iterative(sorted(list98), -1))[1],
                             (binary_search_iterative(sorted(list99), -1))[1], (binary_search_iterative(sorted(list100), -1))[1]))/100)
    
    print "Binary Search Recursive took  %10.7f seconds to run on average" % (sum(((binary_search_recursive(sorted(list1), -1))[1], (binary_search_recursive(sorted(list2), -1))[1], (binary_search_recursive(sorted(list3), -1))[1],
                             (binary_search_recursive(sorted(list4), -1))[1],
                             (binary_search_recursive(sorted(list5), -1))[1],
                             (binary_search_recursive(sorted(list6), -1))[1], (binary_search_recursive(sorted(list7), -1))[1],
                             (binary_search_recursive(sorted(list8), -1))[1], (binary_search_recursive(sorted(list9), -1))[1],
                             (binary_search_recursive(sorted(list10), -1))[1], (binary_search_recursive(sorted(list11), -1))[1],(binary_search_recursive(sorted(list12), -1))[1],
                             (binary_search_recursive(sorted(list13), -1))[1], (binary_search_recursive(sorted(list14), -1))[1],(binary_search_recursive(sorted(list15), -1))[1],
                             (binary_search_recursive(sorted(list16), -1))[1], (binary_search_recursive(sorted(list17), -1))[1],
                             (binary_search_recursive(sorted(list18), -1))[1], (binary_search_recursive(sorted(list19), -1))[1], (binary_search_recursive(sorted(list20), -1))[1],
                             (binary_search_recursive(sorted(list21), -1))[1], (binary_search_recursive(sorted(list22), -1))[1], (binary_search_recursive(sorted(list23), -1))[1],
                             (binary_search_recursive(sorted(list24), -1))[1], (binary_search_recursive(sorted(list25), -1))[1], (binary_search_recursive(sorted(list26), -1))[1],
                             (binary_search_recursive(sorted(list27), -1))[1], (binary_search_recursive(sorted(list28), -1))[1], (binary_search_recursive(sorted(list29), -1))[1],
                             (binary_search_recursive(sorted(list30), -1))[1], (binary_search_recursive(sorted(list31), -1))[1], (binary_search_recursive(sorted(list32), -1))[1],
                             (binary_search_recursive(sorted(list33), -1))[1], (binary_search_recursive(sorted(list34), -1))[1], (binary_search_recursive(sorted(list35), -1))[1],
                             (binary_search_recursive(sorted(list36), -1))[1], (binary_search_recursive(sorted(list37), -1))[1], (binary_search_recursive(sorted(list38), -1))[1],
                             (binary_search_recursive(sorted(list39), -1))[1], (binary_search_recursive(sorted(list40), -1))[1], (binary_search_recursive(sorted(list41), -1))[1],
                             (binary_search_recursive(sorted(list42), -1))[1], (binary_search_recursive(sorted(list43), -1))[1], (binary_search_recursive(sorted(list44), -1))[1],
                             (binary_search_recursive(sorted(list45), -1))[1], (binary_search_recursive(sorted(list46), -1))[1], (binary_search_recursive(sorted(list47), -1))[1],
                             (binary_search_recursive(sorted(list48), -1))[1], (binary_search_recursive(sorted(list49), -1))[1], (binary_search_recursive(sorted(list50), -1))[1],
                             (binary_search_recursive(sorted(list51), -1))[1], (binary_search_recursive(sorted(list52), -1))[1], (binary_search_recursive(sorted(list53), -1))[1],
                             (binary_search_recursive(sorted(list54), -1))[1], (binary_search_recursive(sorted(list55), -1))[1], (binary_search_recursive(sorted(list56), -1))[1],
                             (binary_search_recursive(sorted(list57), -1))[1], (binary_search_recursive(sorted(list58), -1))[1], (binary_search_recursive(sorted(list59), -1))[1],
                             (binary_search_recursive(sorted(list60), -1))[1], (binary_search_recursive(sorted(list61), -1))[1], (binary_search_recursive(sorted(list62), -1))[1],
                             (binary_search_recursive(sorted(list63), -1))[1], (binary_search_recursive(sorted(list64), -1))[1], (binary_search_recursive(sorted(list65), -1))[1],
                             (binary_search_recursive(sorted(list66), -1))[1], (binary_search_recursive(sorted(list67), -1))[1], (binary_search_recursive(sorted(list68), -1))[1],
                             (binary_search_recursive(sorted(list69), -1))[1], (binary_search_recursive(sorted(list70), -1))[1], (binary_search_recursive(sorted(list71), -1))[1],
                             (binary_search_recursive(sorted(list72), -1))[1], (binary_search_recursive(sorted(list73), -1))[1], (binary_search_recursive(sorted(list74), -1))[1],
                             (binary_search_recursive(sorted(list75), -1))[1], (binary_search_recursive(sorted(list76), -1))[1], (binary_search_recursive(sorted(list77), -1))[1],
                             (binary_search_recursive(sorted(list78), -1))[1], (binary_search_recursive(sorted(list79), -1))[1], (binary_search_recursive(sorted(list80), -1))[1],
                             (binary_search_recursive(sorted(list81), -1))[1], (binary_search_recursive(sorted(list82), -1))[1], (binary_search_recursive(sorted(list83), -1))[1],
                             (binary_search_recursive(sorted(list84), -1))[1], (binary_search_recursive(sorted(list85), -1))[1], (binary_search_recursive(sorted(list86), -1))[1],
                             (binary_search_recursive(sorted(list87), -1))[1], (binary_search_recursive(sorted(list88), -1))[1], (binary_search_recursive(sorted(list89), -1))[1],
                             (binary_search_recursive(sorted(list90), -1))[1], (binary_search_recursive(sorted(list91), -1))[1], (binary_search_recursive(sorted(list92), -1))[1],
                             (binary_search_recursive(sorted(list93), -1))[1], (binary_search_recursive(sorted(list94), -1))[1], (binary_search_recursive(sorted(list95), -1))[1],
                             (binary_search_recursive(sorted(list96), -1))[1], (binary_search_recursive(sorted(list97), -1))[1], (binary_search_recursive(sorted(list98), -1))[1],
                             (binary_search_recursive(sorted(list99), -1))[1], (binary_search_recursive(sorted(list100), -1))[1]))/100)
