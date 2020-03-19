class SegmentTree:
    def __init__(self, a):
        self.n = len(a) 
        self.seg = [0] * self.n * 2
        j = self.n
        for i in a:
            self.seg[j] = i
            j += 1

        for i in range(self.n-1, 0, -1):
            self.seg[i] = self.seg[2*i] + self.seg[2*i+1]

        print(self.seg)


    def modify(self, i, val):
        j = self.n + i
        self.seg[j] = val
        j = j // 2
        while j > 0:
            self.seg[j] = self.seg[2*j] + self.seg[2*j+1]
            j = j // 2

        print(self.seg)


    def query(self, a, b):
        l = self.n + a
        r = self.n + b
        res = 0
        while l < r:
            if l & 1: 
                res += self.seg[l]
                l += 1

            if not r & 1:
                res += self.seg[r]
                r -= 1

            l = l // 2
            r = r // 2

        if l == r:
            res += self.seg[l]

        return res 


st = SegmentTree([1,2,3,4,5,6,7,8]) 
#st.modify(0, 2)
res = st.query(2, 5)
assert(res == 36)
