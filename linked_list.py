class LinkedList(object):
    """A singly-linked list."""

    def __init__(self):
        self.head = None

    def __str__(self):
        retval = '('
        nextnode = self.head
        while nextnode:
            if isinstance(nextnode.value, str):
                retval += "'" + nextnode.value + "'"
            else:
                retval += str(nextnode.value)

            if nextnode.next:
                retval += ', '

            nextnode = nextnode.next

        return retval + ')'

    def insert(self, item):
        self.head = LinkedListNode(item, self.head)

    def pop(self):
        popped = self.head
        self.head = self.head.next
        return popped

    def size(self):
        ct = 0
        thisnode = self.head
        while thisnode is not None:
            thisnode = thisnode.next
            ct += 1

        return ct

    def search(self, item):
        thisnode = self.head
        while thisnode is not None:
            if thisnode.value == item:
                return thisnode
            thisnode = thisnode.next
        return None

    def remove(self, item):
        thisnode = self.head
        lastnode = None
        while thisnode:
            if thisnode.value == item:
                #If this was the first item in the LinkedList.
                if not lastnode:
                    self.head = thisnode.next
                #Otherwise, this was not the first item in the LinkedList.
                else:
                    lastnode.next = thisnode.next
                break
            lastnode = thisnode
            thisnode = thisnode.next


class LinkedListNode(object):
    def __init__(self, value=None, nextnode=None):
        self.value = value
        self.next = nextnode

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    pass
    #eventually run some demonstration code here?
