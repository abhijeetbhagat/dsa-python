from threading import Thread
from time import sleep

class Lock:
    def __init__(self):
        self.flag = 0

    def acquire(self):
        while(self.__compare_and_swap(0, 1) == 1):
            continue

    def release(self):
        self.flag = 0

    # overwrite the existing value only if
    # it is equal to the expected value
    def __compare_and_swap(self, expected, new_val):
        original = self.flag
        if self.flag == expected:
            self.flag = new_val
        return original


bal = 500

lock = Lock()

def dec(amt):
    global bal 
    lock.acquire()
    if bal - amt >= 0:
        sleep(1)
        bal -= amt
    lock.release()

threads = [Thread(target=dec, args=[500]), Thread(target=dec, args=[500])]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(bal)
