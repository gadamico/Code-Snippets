def base_converter(n, b):
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    ctr = 0
    N = 1
    while n >= N:
        ctr += 1
        N *= b
    new_rep = ''
    r = 0
    for i in range(1, ctr + 1):
        if int((n - r) / (b ** (ctr - i))) < 10:
            new_rep += str(int((n - r) / (b ** (ctr - i))))
        else:
            new_rep += hex_dict[int((n - r) / (b ** (ctr - i)))]
        if r <= n:
            r += int((n - r) / (b ** (ctr - i))) * (b ** (ctr - i))
    return new_rep
