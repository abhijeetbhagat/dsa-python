import sys
import math

class Fight:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.x = 0
 
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.data = [[sys.maxsize, 0]] * 2 * self.n 
 
    def update(self,left, right, fight, winner):
        left += self.n;
        right += self.n;
 
        while left < right:
            if left & 1:
                self.data[left] = [fight, winner]
                left += 1
            if right & 1:
                right -= 1
                self.data[right] = [fight, winner]
            left >>= 1
            right >>= 1
 
    def query(self,idx):
        idx += self.n
        m = self.data[idx]
 
        while (idx > 1):
            idx >>= 1
            m = min(m, self.data[idx])
 
        return m[1]

n, m = map(int, input().split())
st = SegmentTree(n)
fights = []
for i in range(m):
    f = Fight()
    f.l, f.r, f.x = map(int, input().split())
    fights.append(f)

for i in range(m-1, -1, -1):
    st.update(fights[i].l-1, fights[i].x-1, i, fights[i].x)
    st.update(fights[i].x, fights[i].r, i, fights[i].x)

for i in range(n):
    print(st.query(i), end=' ')

