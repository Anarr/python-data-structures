class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data_val):
        if data_val not in self.stack:
            self.stack.append(data_val)
            return True
        return False

    def peek(self):
        return self.stack[-1]

    def remove(self):
        if len(self.stack) <= 0:
            return "No elements in stack."
        return self.stack.pop()

st = Stack()

st.add("Mon")
st.add("Tue")
print(st.peek())

st.add("Wed")
st.add("Thu")
print(st.peek())

print("=====")
print(st.remove())
print(st.remove())
