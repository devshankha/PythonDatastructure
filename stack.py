class Stack:
    def __init__(self):
        self.mylist = []

    def push(self, element):
        self.mylist.append(element)

    def pop(self):
        return self.mylist.pop()


myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
print(myStack.pop())
print(myStack.pop())