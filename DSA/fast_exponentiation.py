def exp(a, n):
    last_sqr = a
    r = 1
    for i in range(4): # 4 bits for 0 to 15
        next_bit = (n >> i) & 1
        if next_bit:
            r *= last_sqr
        last_sqr *= last_sqr

    return r

assert(exp(4, 15) == 1073741824)
