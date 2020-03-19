class QueueFullException(Exception):
    pass


class QueueEmptyException(Exception):
    pass


class Queue:
    def __init__(self, size=0):
        self.size = size
        self.front = 0
        self.rear = 0
        self.array = [0] * size
        self.count = 0


    def put(self, item):
        if self.count >= self.size:
            raise QueueFullException()

        self.count += 1
        self.array[self.rear] = item
        self.rear += 1
        if self.rear == self.size:
            self.rear = 0


    def get(self):
        if self.count == 0:
            raise QueueEmptyException()

        self.count -= 1

        r = self.array[self.front]
        self.front += 1
        if self.front == self.size:
            self.front = 0

        return r


q = Queue(5)
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
assert(q.get() == 1)
assert(q.get() == 2)
q.put(1)
q.put(2)
q.put(2)
assert(q.get() == 3)
assert(q.get() == 4)
assert(q.get() == 5)
assert(q.get() == 1)
assert(q.get() == 2)
assert(q.get() == 3)

