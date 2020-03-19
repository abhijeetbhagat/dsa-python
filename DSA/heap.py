def heapify(a, i):
    l = 2*i + 1
    r = 2*i + 2
    cur = i
    largest = a[i]
    largest_i = i
    if l < len(a) and a[l] > largest :
        largest = a[l]
        largest_i = l
    if r < len(a) and a[r] > largest:
        largest = a[r]
        largest_i = r
    if largest_i != i:
        a[i], a[largest_i] = a[largest_i], a[i]
        heapify(a, largest_i)

def build_heap(a):
    if not a:
        return
    #index of left child of node i = 2i + 1
    #index of right child of node i = 2i + 2
    #calc index of the last non-leaf node
    last_leaf = len(a) - 1
    i = (last_leaf - 1) // 2
    while i >= 0:
        heapify(a, i)
        i -= 1

a = [4, 10, 3, 5, 1]
build_heap(a)
assert(a == [10, 5, 3, 4, 1])