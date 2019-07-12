def is_sorted(a, i):
    if i + 1 == len(a):
        return True
    return a[i] <= a[i+1] and is_sorted(a, i + 1)


assert(not is_sorted([1,2,3,5,4], 0))
assert(is_sorted([1,2,3,4,5,], 0))
assert(not is_sorted([1,4,3], 0))
assert(is_sorted([1], 0))
assert(is_sorted([1,2], 0))
assert(not is_sorted([2,1,], 0))
