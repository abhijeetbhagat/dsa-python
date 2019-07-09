def partition(a : list, p, r):
    pivot = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1

def quicksort(a, l, h):
    if l < h:
        p = partition(a, l, h)
        quicksort(a, l, p - 1)
        quicksort(a, p + 1, h)
        return a

assert(quicksort([5,4,1,2,3], 0, 4) == [1,2,3,4,5])
