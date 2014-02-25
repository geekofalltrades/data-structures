class Queue(object):
    """A classic queue data structure."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def queue(self, value):
        """Add an object to the head of the queue."""
        oldhead = self.head
        self.head = QueueNode(value, next=oldhead)
        if oldhead:
            oldhead.prev = self.head
        else:
            self.tail = self.head
        self._size += 1

    def dequeue(self):
        """Remove and return an item from the tail of the queue."""
        dequeued = self.tail
        if not dequeued:
            raise EmptyError("Attempted to dequeue from empty queue.")

        self._size -= 1

        self.tail = dequeued.prev
        if dequeued.prev:
            dequeued.prev.next = None

        if self.head is dequeued:
            self.head = self.tail

        return dequeued.value

    def size(self):
        """Return the size of the queue."""
        return self._size


class QueueNode(object):
    """Nodes for the queue - essentially doubly-linked-list nodes."""

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class EmptyError(BaseException):
    """Exception raised when attempting to dequeue from an empty queue.
    """
    pass
