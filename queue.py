class Queue:
    def __init__(self):
        self.queue = []

    def add(self, data_val):
        if data_val is not self.queue:
            self.queue.insert(0,data_val)
            return True
        return False

    def size(self):
        return len(self.queue)

    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "No elements in Queue!"
q = Queue()

q.add("Mon")
q.add("Tue")
q.add("Wed")

print(q.size())

print(q.remove())
print(q.remove())