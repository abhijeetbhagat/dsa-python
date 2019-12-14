from fnv import fnv
import mmh3

class BloomFilter:
    def __init__(self):
        self.buckets_size = 10
        self.buckets = [0] * self.buckets_size

    def insert(self, key):
        i = fnv(key, 32) % self.buckets_size
        k = abs(mmh3.hash(key)) % self.buckets_size
        print(f"insert: for key {key}, fnv index = {i}, mmh3 index = {k}")
        self.buckets[i] = 1
        self.buckets[k] = 1

    def contains(self, key):
        i = fnv(key, 32) % self.buckets_size
        k = abs(mmh3.hash(key)) % self.buckets_size
        print(f"contains: for key {key}, fnv index = {i}, mmh3 index = {k}")
        if self.buckets[i] == 1 and self.buckets[k] == 1:
            return True
        else:
            return False
 
class PornFilter:
    def __init__(self):
        self.bf = BloomFilter()
        # build our black list
        self.bf.insert("pornhub")
        self.bf.insert("xxxvidz")
        self.bf.insert("brazzers")
        self.bf.insert("xnxx")

    def matches(self, domain):
        return self.bf.contains(domain)


pf = PornFilter()
print(f"Brazzers is a porn site ? {pf.matches('brazzers')}") 
print(f"Reddit is a porn site ? {pf.matches('reddit')}") 
print(f"GPAC is a porn site ? {pf.matches('gpac')}") 
print(f"xnxx is a porn site ? {pf.matches('xnxx')}") 
print(f"hackernews is a porn site ? {pf.matches('hackernews')}") 