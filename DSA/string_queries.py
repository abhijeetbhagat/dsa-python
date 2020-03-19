class SegmentTree:
    def __init__(self, a): 
        self.n = len(a)
        self.seg = [0] * self.n * 2
        i = self.n
        for c in a:
            self.seg[i] = 1 << (ord(c) - 97)
            i += 1

        for i in range(self.n-1, 0, -1):
            self.seg[i] = self.seg[2*i] | self.seg[2*i+1]
 
    def modify(self, i, v): 
        p = self.n + i
        self.seg[p] = 1 << (ord(v) - 97)
        p = p // 2
        while p > 0:
            self.seg[p] = self.seg[2*p] | self.seg[2*p+1]
            p = p // 2
 
 
    def query(self, p, q):
        l = self.n+p
        r = self.n+q
        res = 0
        while l < r:
            if l & 1: 
                res |= self.seg[l]
                l += 1
            if not r & 1:
                res |= self.seg[r]
                r -= 1

            l = l // 2
            r = r // 2

        if l == r:
            res |= self.seg[l]

        return res
 
N = int(input())
S = [c for c in input()]
Q = int(input())

st = SegmentTree(S)
r = []

for i in range(Q):
    p, a, b = input().split()
    if p == '1':
        st.modify(int(a)-1, b)
    else:
        r.append(bin(st.query(int(a)-1, int(b)-1)).count('1'))

for v in r:
    print(v)
