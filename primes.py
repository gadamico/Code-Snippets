def k_primes(k, start, stop):
    """
    This function will return the k-primes between start and stop (inclusive).
    (A k-prime for natural k is a natural number with k prime divisors, counting multiplicity.
    So 4, 5, 6, 7, 8 are a 2-prime, a 1-prime (i.e. prime), a 2-prime, a 1-prime, and a 3-prime,
    respectively.)
    """
    ks = []
    for i in range(start, stop + 1):
        primes = [2]
        primes.extend(range(3, int(i / 2) + 1, 2))
        ctr = 0
        for num in primes:
            
            while i % num == 0:
                ctr += 1
                i /= num
        if ctr == 0:
            ctr = 1
        ks.append(ctr)
    indices = [i for i, x in enumerate(ks) if x == k]    
    return [start + index for index in indices]




def IsPrime(n):
    """
    This function computes whether an input number is prime or not.
    """
    if n == 1:
        out = False
    else:
        for ctr in range(2, int(n**0.5) + 1):
            if n % ctr == 0:
                out = False
                return out
        out = True
    return out




def p_fact(n):
    facts = []
    for num in range(2, n + 1):
        if IsPrime(num):
            if n % num == 0:
                facts.append(1)
                n /= num
                while n % num == 0:
                    facts[-1] += 1
                    n /= num
            else:
                facts.append(0)
    if sum(facts) == 0:
        facts = []
    if len(facts) != 0:
        while facts[-1] == 0:
            del facts[-1]
    return facts




def kPrimesLeadCounter(n):
    test = 2
    ctr = 0
    while n >= test:
        test *= 2
        ctr += 1
    nums = list(np.zeros(ctr))
    nums[0] = 1
    i = 3
    pos = nums.index(int(max(nums)))
    new_pos = pos
    while sum(nums) + 2 <= n:
        if new_pos == pos:
            nums[sum(p_fact(i)) - 1] += 1
            i += 1
            if  nums.count(int(max(nums))) == 1:
                new_pos = nums.index(int(max(nums)))
        else:
            print(int(sum(nums) + 1), [int(num) for num in nums])
            pos = new_pos
    return [int(num) for num in nums]




def factorize(num):
    import json
    with open('prime_factorizations_19999.json', 'r') as f:
        facts = json.load(f)
    with open('primes_19999.json', 'r') as g:
        primes = json.load(g)
    list_ = facts[str(num)]
    last = len(list_)
    map_ = zip(list_, primes[:last])
    out = []
    for expon, prime in map_:
        if expon == 0:
            pass
        elif expon == 1:
            out.append(str(prime))
        else:
            out.append(str(prime) + '^' + str(expon))
    return '*'.join(out)