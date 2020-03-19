from threading import Thread
from time import sleep

class Lock:
    def __init__(self):
        self.ticket = 0
        self.turn = 0

    def acquire(self):
        my_turn = self.__fetch_and_add()
        while self.turn != my_turn:
            continue

    def release(self):
        self.turn += 1

    # just increment ticket by one
    # and return the pre-incremented ticket
    # also called as the ticket lock
    def __fetch_and_add(self):
        original = self.ticket
        self.ticket += 1
        return original


lock = Lock()

bal = 500

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
