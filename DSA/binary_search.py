def binary_search_recursive(a : list, key : int, l : int, h : int):
    if l > h:
        return -1
    m = (l + h) // 2
    if a[m] == key:
        return m
    if a[m] > key:
        h = m - 1
    else:
        l = m + 1
    return binary_search_recursive(a, key, l, h)

def binary_search(a, key):
    return binary_search_recursive(a, key, 0, len(a) - 1)

assert(binary_search([1,2,3,4,5], -1) == -1)
assert(binary_search([1,2,3,4,5], 1) == 0)
assert(binary_search([1,2,3,4,5], 3) == 2)
assert(binary_search([1,2,3,4,5], 4) == 3)
assert(binary_search([1,2,3,4,5], 5) == 4)
