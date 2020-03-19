line = input().split()
N = int(line[0])
M = int(line[1])

a = [-1] * 5
for i in range(M):
    line = input().split()
    s = line[0]
    c = line[1]
    if a[s] != -1 and a[s] != c:
        print(-1)
        break
    else:
        a[s] = c


