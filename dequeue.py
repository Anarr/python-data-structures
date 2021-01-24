import collections

d_ended = collections.deque(["Mon", "Tue", "Wed"])

d_ended.append("Thu")

print("appended at right -")
print(d_ended)

d_ended.appendleft("Sun")

print("appended at left -")
print(d_ended)


d_ended.pop()

print("deleted from right -")
print(d_ended)

d_ended.popleft()

print("deleted from left -")
print(d_ended)