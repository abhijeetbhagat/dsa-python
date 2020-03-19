from threading import Lock, Thread

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass


class TSQueue:
    def __init__(self, size):
        self.size = size
        self.array = [0] * size
        self.front = 0
        self.rear = 0
        self.count = 0
        self.lock = Lock()

    def try_put(self, item):
        if self.count >= self.size:
            raise QueueFullException()

        lock.acquire()
        try:
            self.count += 1
            self.array[self.rear] = item
            self.rear += 1

            if self.rear == self.size:
                self.rear = 0
        finally:
            lock.release()

    def try_get(self):
        if self.count == 0:
            raise QueueEmptyException()

        self.count -= 1
        item = self.array[self.front]
        self.front += 1
        if self.front == 0:
            self.front = 0

        return item

def enqueue():
    pass

# threads = [Thread(target=enqueue), Thread(target=enqueue)]

q = TSQueue(4)
q.try_put(1)
q.try_put(2)
assert(q.try_get() == 1)
assert(q.try_get() == 2)
q.try_put(3)
q.try_put(4)
assert(q.try_get() == 3)
assert(q.try_get() == 4)
