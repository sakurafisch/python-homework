from Stack import Stack

s: Stack = Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek(0))
s.push(True)
print(s.size(0))
print(s.isEmpty())
s.push(8.4)
print(s)
print(s.pop())
print(s.pop())
print(s.size())
print(s)
