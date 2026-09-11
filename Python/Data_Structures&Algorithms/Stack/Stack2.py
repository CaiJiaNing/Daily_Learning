class Stack:
    # Implement the stack as a list
    # Take the first element of the list as the top of the stack
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)
    # Check if the stack is empty

    def push(self, item):
        self._items.insert(0, item)
    # Add an element to the stack
    
    def pop(self):
        return self._items.pop(0)
    # Remove the top element of the stack
    
    def peek(self):
        return self._items[0]
    # Get the top element of the stack
    
    def size(self):
        return len(self._items)
    # Get the number of elements in the stack