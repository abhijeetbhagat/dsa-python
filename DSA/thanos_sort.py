'''
Thanos sort is a supervillain sorting algorithm, which works as follows: if the array is not sorted, snap your fingers*
to remove the first or the second half of the items, and repeat the process.  
Given an input array, what is the size of the longest sorted array you can obtain from it using Thanos sort?  

*Infinity Gauntlet required.
'''

def is_sorted(a, i):
    if i + 1 is len(a):
        return True
    return a[i] < a[i+1] and is_sorted(a, i+1)

def thanos_sort(a):
    if is_sorted(a, 0):
        return len(a)
    else:
        mid = len(a) // 2
        lhl = thanos_sort(a[:mid])
        rhl = thanos_sort(a[mid:])
        if lhl > rhl:
            return lhl
        else:
            return rhl

assert(thanos_sort([1,2,3,4]) == 4)
assert(thanos_sort([1,2,4,3]) == 2)
assert(thanos_sort([7,6,5,4]) == 1)
assert(thanos_sort([11,12,1,2,13,14,3,4]) == 2)
assert(thanos_sort([1]) == 1)
