def insertion_sort(a):
    for i in range(len(a)):
        temp = a[i]
        j = i
        while j > 0 and temp < a[j - 1]:
            a[j] = a[j - 1]
            j -= 1
        a[j] = temp

    return a

assert(insertion_sort([5,4,3,2,1]) == [1,2,3,4,5])
