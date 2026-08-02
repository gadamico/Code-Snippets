def productFib(prod):

    # We'll begin by initializing two arrays, one
    # for the Fibonacci numbers up to the square
    # root of our input (any further and the products
    # of consecutive Fibonacci numbers will forever
    # be larger than our input), and one for our
    # output.
    
    fib = []
    arr = []
    
    # We'll feed in the first two numbers in the
    # Fibonacci sequence.
    
    fib.extend([0, 1])
    
    # And fill it in until we reach the square root
    # of the input.
    
    while fib[-1] <= int(prod ** 0.5):
        fib.append(fib[-1] + fib[-2])
    
    # Now we need to check fib, looking for
    # consecutive numbers with a product of prod.
    # If we find it, we'll just return it immediately.
    
    for i in range(len(fib) - 1):
        if fib[i] * fib[i + 1] == prod:
            arr.extend([fib[i], fib[i + 1], True])
            return arr
    
    # If not, then we'll prepare our output accordingly.
    # We may need to add one more number in our
    # sequence. We'll check that first.
    
    if fib[-1] * fib[-2] < prod:
        fib.append(fib[-1] + fib[-2])
    arr.extend([fib[-2], fib[-1], False])
    return arr
