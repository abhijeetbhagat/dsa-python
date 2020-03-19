a = [0,1,3,4]
def find_val(i):
    global a
    if i > 0:
        s = i // 4
        return a[i%4] + ((s * (s + 1)) // 2)
    else:
        return 0

#r = find_val(5)
#assert(r == 3)
num = int(input())
r = []
for _ in range(num):
    r.append(find_val(int(input())))
for o in r:
    print(o)

