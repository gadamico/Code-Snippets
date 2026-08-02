def whoIsNext(names, r):
    
    # We need to figure out how many doublings have happened. The first
    # round of doubling happens after 5 colas; the second after 15. In
    # general, doubling happens after 2 * n + 5 colas, where n is the
    # number of colas before the previous doubling. So we'll count
    # the doublings.
    
    i = 5
    j = 1
    print(r)
    while r > i:
        i = 2 * i + 5
        j *= 2
    
    # Now: if r is less than j more than the number of the last
    # doubling, we'll know it's Sheldon. If it's greater than that
    # but less than 2j more than the number of the last doubling,
    # we'll know it's Leonard. Etc.
    
    if (r < (i - 6) / 2 + j) | (r == 1):
        pers = 'Sheldon'
    elif (r < (i - 6) / 2 + 2 * j) | (r == 2):
        pers = 'Leonard'
    elif (r < (i - 6) / 2 + 3 * j) | (r == 3):
        pers = 'Penny'
    elif (r < (i - 6) / 2 + 4 * j) | (r == 4):
        pers = 'Rajesh'
    else:
        pers = 'Howard'
    return pers
