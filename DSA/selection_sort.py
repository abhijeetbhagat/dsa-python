def selection_sort(a):
    for i in range(len(a)):
        min_i = i
        for k in range(i+1, len(a)):
            if a[min_i] > a[k]:
                min_i = k
        a[i], a[min_i] = a[min_i], a[i]
    return a

assert(selection_sort([5,4,3,2,1]) == [1,2,3,4,5])
