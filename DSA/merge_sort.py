def merge(o, a, b):
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            o[k] = a[i]
            i += 1
        else:
            o[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        o[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        o[k] = b[j]
        j += 1
        k += 1

def merge_sort(a): 
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(a, left, right)
        return a

assert(merge_sort([5,4,3,2,1]) == [1,2,3,4,5])
