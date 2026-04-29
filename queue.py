# Queue digunakan untuk:
# - Soal 2 & 3 (manual)
# - Soal 4 & 5 (simulasi)
# - Soal 6 (reverse queue)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None  # sederhana untuk tugas

    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Soal 6: Reverse Queue
def reverse_queue(q):
    stack = []

    while not q.isEmpty():
        stack.append(q.dequeue())

    while stack:
        q.enqueue(stack.pop())

    return q