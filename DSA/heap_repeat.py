def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i-1)//2

#max heapifies tree(array) a at node(index) i
def max_heapify(a, i):
    #get the indices of the children of i
    l = left(i)
    r = right(i)

    #compare the three - node, its left and its right
    #to find which one is bigger
    largest_index = -1
    if l < len(a) and a[l] > a[i]: 
        largest_index = l
    else:
        largest_index = i

    if r < len(a) and a[r] > a[largest_index]:
        largest_index = r

    #swap the largest with the node
    #and start max_heapifying downwards from the largest_index
    if largest_index is not i:
        a[i], a[largest_index] = a[largest_index], a[i]
        max_heapify(a, largest_index)

def min_heapify(a, i):
    #get the indices of the left and right children
    #of the current node (i)
    l = left(i)
    r = right(i)

    #get the index of the smallest of the three
    smallest_index = -1
    if l < len(a) and a[l] < a[i]:
        smallest_index = l
    else:
        smallest_index = i

    if r < len(a) and a[r] < a[smallest_index]:
        smallest_index = r

    #swap the current with smallest
    if smallest_index != i:
        a[i], a[smallest_index] = a[smallest_index], a[i]
        min_heapify(a, smallest_index)

#this builds a binary max heap in-place from a binary tree 'a'
#by continuously calling max_heapify starting from
#the last non-leaf node (or parent of the last leaf),
#visiting all the non-leaf nodes at all levels one level at a time all
#the way up to the root
def build_heap(a):
    #get the index of the last leaf node
    last_leaf_index = (len(a) - 1) // 2
    #get the index of the parent of the last leaf node
    parent_index = parent(last_leaf_index) 
    while (parent_index >= 0):
        max_heapify(a, parent_index)
        parent_index -= 1

a = [1, 14, 10, 8, 7, 9, 3, 2, 4, 6]
max_heapify(a, 0)
assert(a == [14, 8, 10, 4, 7, 9, 3, 2, 1, 6])
a = [4, 10, 3, 5, 1]
build_heap(a)
assert(a == [10, 5, 3, 4, 1])
assert(parent(4) == 1)
assert(parent(1) == 0)
assert(parent(2) == 0)
