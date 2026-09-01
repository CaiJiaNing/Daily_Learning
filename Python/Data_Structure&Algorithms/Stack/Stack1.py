class Stack:
    # Implement the stack as a list
    # Take the first element of the list as the bottom of the stack
    def __init__(self):
        self._items = []
    # Create a new stack

    def is_empty(self):
        return not bool(self._items)
    # Check if the stack is empty
    # Empty stack returns True, otherwise returns False

    def push(self, item):
        self._items.append(item)
    # Add an element to the stack

    def pop(self):
        return self._items.pop()
    # Remove the top element of the stack

    def peek(self):
        return self._items[-1]
    # Get the top element of the stack

    def size(self):
        return len(self._items)
    # Get the number of elements in the stack