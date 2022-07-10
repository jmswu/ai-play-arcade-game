from datetime import datetime
import time

class Test:
    def __init__(self) -> None:
        self._count = 0

    def increase(self) -> None:
        self._count = self._count + 1

    def printCount(self) -> None:
        print(f'count is {self._count}')

t = Test()

t.increase()
t.printCount()

start = time.time()

loop = 0xffff
while(loop != 0):
    loop = loop -1
diff = time.time() - start

print(diff)
