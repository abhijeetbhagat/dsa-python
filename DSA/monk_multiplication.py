"""
The Monk learned about priority queues recently and asked his teacher for an interesting problem. So his teacher came up with a simple problem. He now has an integer array A. For each index i, he wants to find the product of the largest, second largest and the third largest integer in the range [1,i].
Note: Two numbers can be the same value-wise but they should be distinct index-wise.

Input:
The first line contains an integer N, denoting the number of elements in the array A.
The next line contains N space separated integers, each denoting the ith integer of the array A.

Output:
Print the answer for each index in each line. If there is no second largest or third largest number in the array A upto that index, then print "-1", without the quotes.

Constraints:
1 <= N <= 100000
0 <= A[i] <= 1000000

SAMPLE INPUT 
5
1 2 3 4 5
SAMPLE OUTPUT 
-1
-1
6
24
60
Explanation
There are 5 integers 1,2,3,4 and 5.
For the first two indexes, since the number of elements is less than 3, so -1 is printed.
For the third index, the top 3 numbers are 3,2 and 1 whose product is 6.
For the fourth index, the top 3 numbers are 4,3, and 2 whose product is 24.
For the fifth index, the top 3 numbers are 5,4 and 3 whose product is 60.
"""

hs = 4


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def heap_size():
    return hs


def parent(i):
    return (i-1) // 2


def max_heapify(a, i):
    # get left and right indices
    l = left(i)
    r = right(i)

    # get the largest of the three
    largest_index = -1
    if l <= heap_size() and a[l] > a[i]:
        largest_index = l
    else:
        largest_index = i

    if r <= heap_size() and a[r] > a[largest_index]:
        largest_index = r

    # swap largest with current
    if largest_index != i:
        a[i], a[largest_index] = a[largest_index], a[i]
        max_heapify(a, largest_index)


def product(a):
    result = []
    if len(a) < 3:
        result = [-1] * len(a)
    elif len(a) == 3:
        result = [-1,-1,a[0]*a[1]*a[2]]
    else:
        result = [-1,-1,a[0]*a[1]*a[2]]
        for i in range(3, len(a)):
            global hs
            hs = i
            
            parent_index = parent(i)
            while parent_index >= 0:
                max_heapify(a, parent_index)
                parent_index -= 1

            result.append(a[0]*a[1]*a[2])
    return result


from operator import mul
from functools import reduce

def product_sort(a):
    result = []
    if len(a) < 3:
        result = [-1] * len(a)
    else:
        result = [-1, -1]
        a.sort()
        j = 3
        for i in range(0, len(a) - 2):
            result.append(reduce(mul, a[i:j]))
            j += 1

    return result


a = [1,2,3,4,5]
result = product_sort(a)
assert(result == [-1,-1,6,24,60])

a = [1,2,3,4,5]
result = product(a)
assert(result == [-1,-1,6,24,60])

a = []
result = product(a)
assert(result == [])

a = [1,2]
result = product(a)
assert(result == [-1,-1])

a = [1,2,3]
result = product(a)
assert(result == [-1,-1,6])
