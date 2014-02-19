class LinkedList(object):
    def __init__(self):
        self.head = None

    def __str__(self):
        retval = []
        nextnode = self.head
        while nextnode != None:
            retval.append(nextnode.value)
            nextnode = nextnode.next

        return retval

    def count(self):
        ct = 0
        nextnode = self.head
        while nextnode != None:
            nextnode = nextnode.next
            ct += 1

        return ct

    def find(self, findval):
        nextnode = self.head
        while nextnode != None:
            if nextnode.value == findval:
                return True
        return False

    def remove(self, item):
        pass


class LinkedListNode(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


if __name__ == '__main__':
    pass
    #eventually run some demonstration code here?