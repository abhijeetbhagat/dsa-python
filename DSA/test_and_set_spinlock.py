from threading import Thread
import time


class Data:
    def __init__(self, val):
        self.val = val


class Lock:
    def __init__(self):
        self.d = Data(0)


    # just overwrite the existing value with
    # the new one
    def __test_and_set(self, new_val: int) -> int:
        old = self.d.val
        self.d.val = new_val
        return old


    def acquire(self):
        while self.__test_and_set(1) == 1:
            continue


    def release(self):
        self.d.val = 0


a = 500
def inc(amt):
    global a
    a += amt

lock = Lock()

def dec(amt):
    global a
    lock.acquire()
    if a - amt >= 0: 
        time.sleep(1)
        a -= amt
    lock.release()


threads = [Thread(target=dec, args=[500]), Thread(target=dec, args=[500])]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(a)

