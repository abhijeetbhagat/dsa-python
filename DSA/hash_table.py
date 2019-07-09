class LinkedList:
    class Node:
        def __init__(self, v):
            self.value = v
            self.next = None

    def __init__(self):
        self.__head = None

    def add(self, value):
        if self.__head is None:
            self.__head = LinkedList.Node(value)
        else:
            p = self.__head
            while p.next is not None :
                p = p.next
            p.next = LinkedList.Node(value)

    def find(self, value):
        p = self.__head
        while p is not None:
            if p.value[0] == value:
                return p.value[1]
            p = p.next
        return None
            

class HashMap:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__buckets = [None] * capacity
    
    def add(self, key, val):
        bucket = hash(key) % self.__capacity
        if self.__buckets[bucket] is None:
            ll = LinkedList()
            ll.add((key, val))
            self.__buckets[bucket] = ll
        else:
            self.__buckets[bucket].add((key, val))

    def get(self, key):
        bucket = hash(key) % self.__capacity
        if self.__buckets[bucket] is None:
            return None
        else:
            return self.__buckets[bucket].find(key)

#ll = LinkedList()
#ll.add(("abhi", 1))
#ll.add(("dsa", 2))
#assert(ll.find("abhi") == 1)
#assert(ll.find("dsa") == 2)
#assert(ll.find("assert") == None)
h = HashMap(10)
h.add("abhi", 1)
h.add("dsa", 2)
assert(h.get("abhi") == 1)
assert(h.get("dsa") == 2)
assert(h.get("timsort") == None)

