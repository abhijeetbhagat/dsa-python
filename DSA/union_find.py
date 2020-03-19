class UnionFind:
    def __init__(self, n):
        self.sets = [i for i in range(n)]
        self.cc_count = [1] * n

    def unite(self, a, b):
        x = self.find_rep(a)
        y = self.find_rep(b)
        if x != y:
            if self.cc_count[x] >= self.cc_count[y]:
                self.sets[y] = x
                self.cc_count[x] += self.cc_count[y]
            else:
                self.sets[x] = y
                self.cc_count[y] += self.cc_count[x]

    def find_rep(self, a):
        if self.sets[a] == a:
            return a
        return self.find_rep(self.sets[a])

n, r, d = map(int, input().split())
uf = UnionFind(n+1)
for _ in range(r):
    a, b = map(int, input().split())
    uf.unite(a, b)

for i in range(1, n+1): 
    r = uf.find_rep(i)
    print(uf.cc_count[r] - 1, end=' ')

print("")
