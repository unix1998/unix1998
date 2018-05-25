#! /usr/local/bin/python3
import queue

q = queue.LifoQueue()

for i in range(10):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')

print()
print()
print()
