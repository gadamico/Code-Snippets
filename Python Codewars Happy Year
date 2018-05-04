def next_happy_year(year):
    # We begin by adding 1 to our input and then
    # turning it into a string.
    
    next = str(year + 1)
    
    # We'll initialize a list to count the occurrences of each symbol.
    
    cts = []
    while int(next) < 10000:
        for s in next:
            cts.append(next.count(s))
            
        # Here's the key step: We use list comprehension to check if each
        # symbol occurs less than twice (i.e. only once!).
        
        if all([x < 2 for x in cts]):
            break
        else:
        
            # If it doesn't work then we do it over again.
            
            cts = []
            next = str(int(next) + 1)
    return int(next)   
