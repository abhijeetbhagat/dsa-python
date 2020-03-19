#         4
#       /   \
#      3     7
#     / \   / \
#    1   2 3   4

class SegTree:
    def __init__(self, a):
        self.n = len(a)
        self.seg = [0] * 2 * self.n
        j = self.n
        for v in a:
            self.seg[j] = v
            j += 1

        j = self.n // 2
        k = 0
        for i in range(self.n - 1, 0, -1):
            self.seg[i] = self.seg[2*i] | self.seg[2*i+1] if i >= j and not k & 1 else self.seg[2*i] ^ self.seg[2*i+1]
            if i == j:
                j = j // 2
                k += 1

    def modify(self, i , val):
        p = self.n + i
        self.seg[p] = val
        p = p // 2
        j = 0
        while p > 0:
            self.seg[p] = self.seg[2*p] | self.seg[2*p+1] if not j & 1 else self.seg[2*p] ^ self.seg[2*p+1]
            p = p // 2
            j += 1

    def query(self):
        return self.seg[1]


n, m = map(int, input().split())
a = list(map(int, input().split()))
st = SegTree(a)
r = []

for _ in range(m):
   i, v = map(int, input().split())
   st.modify(i-1, v)
   r.append(st.query())

for i in r:
    print(i)


