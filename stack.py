class Stack(object):
    """The classic stack data structure."""
    def __init__(self):
        self.head = None

    def push(self, value):
        self.head = StackNode(value, self.head)

    def pop(self):
        if self.head:
            popped, self.head = self.head, self.head.next
            return popped.value


class StackNode(object):
    """Individual nodes representing data objects stored in the stack."""
    def __init__(self, value=None, nextnode=None):
        self.value = value
        self.next = nextnode

    def __str__(self):
        return str(self.value)
