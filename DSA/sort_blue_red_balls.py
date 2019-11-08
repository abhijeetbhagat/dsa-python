#a list of red and blue balls; sort it such that red balls
#are stored first. 0 means red, 1 means blue, a is the list.
def sort_balls(a):
    i = 0
    j = len(a) - 1
    if(not a):
        return

    while(i < len(a)//2 or i < j):
        while(a[i] != 1 and i < len(a) // 2):
            i += 1
        while(a[j] != 0 and j >= 0):
            j -= 1
        if(i == j or j < i):
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return a
        
b = [1, 0, 1, 0, 1]
sort_balls(b)
assert(b == [0, 0, 1, 1, 1])
b = [1, 0, 1, 0]
sort_balls(b)
assert(b == [0, 0, 1, 1])
b = [0, 0, 1, 1]
sort_balls(b)
assert(b == [0, 0, 1, 1])
b = [0, 0]
sort_balls(b)
assert(b == [0, 0])
