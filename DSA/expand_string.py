def find_nth(input: str, n): 
    i = 1
    j = 0
    lim = len(input) // 2
    total_freq = 0
    while j < lim:
        cur_char = input[i-1]
        freq = int(input[i])
        total_freq += freq
        if n <= total_freq:
            return cur_char

        i += 2
        j += 1

    return -1


assert(find_nth("a3b4", 5) == 'b')
assert(find_nth("a3b3", 3) == 'a')
assert(find_nth("a3b3", 10) == -1)
