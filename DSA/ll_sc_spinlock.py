from threading import Thread
from time import sleep

class Lock:
    def __init__(self):
        self.val = 0


    def acquire(self):
        self.__load_linked()
        while self.__store_conditional(1) == 1:
            val = self.__load_linked()
            continue


    def release(self):
        self.val = 0


    def __load_linked(self):
        return self.val


    def __store_conditional(self, val):
        if self.val == self.__load_linked():
            self.val = val
            return 1
        else:
            return 0


bal = 500

def dec(amt):
    global bal
    if bal - amt >= 0:
        bal -= amt

threads = [Thread(target=dec, args=[500]), Thread(target=dec, args=[500])]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(bal)
