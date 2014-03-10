import unittest
from data_structures.queue import Queue, EmptyError


class TestQueue(unittest.TestCase):
    """Test the queue method of the queue."""

    def setUp(self):
        self.values = ['bob', 'fred', range(3), 3.14]
        self.single_value = 'teststring'

    def test_queue_to_empty_queue(self):
        """Queue a value on an empty queue."""
        q = Queue()
        self.assertTrue(q.head is None)
        self.assertTrue(q.tail is None)
        q.queue(self.single_value)
        self.assertEqual(q.head.value, self.single_value)
        self.assertEqual(q.tail.value, self.single_value)
        self.assertTrue(isinstance(q.head.value, type(self.single_value)))

    def test_queue_to_populated_queue(self):
        """Queue a value on a populated queue."""
        q = Queue()
        self.assertTrue(q.head is None)
        self.assertTrue(q.tail is None)
        for val in self.values:
            q.queue(val)
        self.assertEqual(q.head.value, self.values[-1])
        self.assertEqual(q.tail.value, self.values[0])
        self.assertTrue(isinstance(q.head.value, type(self.values[-1])))
        self.assertTrue(isinstance(q.tail.value, type(self.values[0])))


class TestDequeue(unittest.TestCase):
    """Test the dequeue method of the queue."""

    def setUp(self):
        self.values = ['bob', 'fred', range(3), 3.14]
        self.single_value = 'teststring'

    def test_dequeue_from_empty_queue(self):
        """Dequeue a value from an empty queue."""
        q = Queue()
        self.assertTrue(q.head is None)
        self.assertTrue(q.tail is None)
        self.assertRaises(EmptyError, q.dequeue)

    def test_dequeue_from_populated_queue(self):
        """Dequeue a value from a populated queue."""
        q = Queue()
        q.queue(self.single_value)
        dequeued = q.dequeue()
        self.assertEqual(dequeued, self.single_value)
        self.assertTrue(isinstance(dequeued, type(self.single_value)))

    def test_dequeue_last_item_from_queue(self):
        """Dequeue a value from a queue that contains only one item."""
        q = Queue()
        self.assertTrue(q.head is None)
        self.assertTrue(q.tail is None)
        q.queue(self.single_value)
        q.dequeue()
        self.assertTrue(q.head is None)
        self.assertTrue(q.tail is None)


class TestSize(unittest.TestCase):
    """Test the size method of the queue."""

    def setUp(self):
        self.values = ['bob', 'fred', range(3), 3.14]
        self.single_value = 'teststring'

    def test_size_of_empty_queue(self):
        """Take the size of an empty queue."""
        q = Queue()
        self.assertTrue(q.head is None)
        self.assertTrue(q.tail is None)
        self.assertEquals(q.size(), 0)

    def test_size_of_populated_queue(self):
        """Take the size of a populated queue."""
        q = Queue()
        for val in self.values:
            q.queue(val)
        self.assertEqual(q.size(), len(self.values))

    def test_size_of_depopulated_queue(self):
        """Take the size of a queue that has been populated and then had
        some items dequeued."""
        q = Queue()
        for val in self.values:
            q.queue(val)
        q.dequeue()
        self.assertEqual(q.size(), len(self.values) - 1)

    def test_size_of_empty_queue_popped_from(self):
        """Take the size of a queue that has been dequeued from its empty
        state."""
        q = Queue()
        self.assertRaises(EmptyError, q.dequeue)
        self.assertEqual(q.size(), 0)


if __name__ == '__main__':
    unittest.main()
