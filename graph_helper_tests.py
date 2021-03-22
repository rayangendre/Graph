import unittest
from graph import *
from stack_array import Stack
from queue_array import Queue


class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])

    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_03(self):
        with self.assertRaises(FileNotFoundError):
            g = Graph('doesnotexist.txt')

    def test_04(self):
        g = Graph('upper_number.txt')
        self.assertEqual(g.conn_components(), [['v10', 'v1000', 'v1200'],['v200'], ['v30', 'v49', 'v50']])
        self.assertFalse(g.is_bipartite())

    def test_05(self):
        g = Graph('single.txt')
        self.assertEqual(g.conn_components(), [['v1']])

        self.assertEqual(g.get_vertices(), ['v1'])
        self.assertEqual(g.get_vertex('v2'), None)

    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)

    def test_simple_2(self):
        # checks that the pop and isEmpty method are working
        stack = Stack(7)
        stack.push(3)
        self.assertFalse(stack.is_empty())
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_simple_3(self):
        # checks the is_full method for working
        stack = Stack(1)
        stack.push(4)
        self.assertTrue(stack.is_full)

    def test_simple_4(self):
        # checks the peek method
        stack = Stack(0)
        with self.assertRaises(IndexError):
            stack.peek()

        stack = Stack(7)
        stack.push(4)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        stack.pop()
        self.assertEqual(stack.peek(), 4)

    def test_simple_5(self):
        # testing of the push method
        stack = Stack(2)
        stack.push(3)
        stack.push(2)
        with self.assertRaises(IndexError):
            stack.push(4)

    def test_simple_6(self):
        # testing of the pop method
        stack = Stack(0)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_simple_7(self):
        # testing of none
        stack = Stack(None)
        with self.assertRaises(IndexError):
            stack.push('hello')

    def test_simple_8(self):
        stack = Stack(0)
        self.assertTrue(stack.is_full)

    def test_queue_1(self):
        # testing the isEmpty and is full methods
        queue = Queue(0)
        self.assertTrue(queue.is_empty())

        queue = Queue(1)
        queue.enqueue('hey')
        self.assertTrue(queue.is_full())
        self.assertFalse(queue.is_empty())

    def test_queue_2(self):
        # checks the raise Index error Fucntions
        queue = Queue(None)
        with self.assertRaises(IndexError):
            queue.enqueue('a')
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_queue_3(self):
        # checks the dequeue and enqueue methods are working together well
        queue = Queue(2)
        queue.enqueue('first')
        queue.enqueue('second')
        self.assertEqual(queue.dequeue(), 'first')
        self.assertEqual(queue.dequeue(), 'second')

    def test_queue_4(self):
        q = Queue(2)
        self.assertEqual(q.size(), 0)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)

    def test_queue_5(self):
        q = Queue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        q.enqueue('a')
        q.enqueue('b')
        self.assertEqual(q.dequeue(), 'a')
        self.assertEqual(q.dequeue(), 'b')

    def test_queue_6(self):
        q = Queue(0)
        with self.assertRaises(IndexError):
            q.enqueue('hello')

    def test_queue_7(self):
        q = Queue(1)
        with self.assertRaises(IndexError):
            q.dequeue()


if __name__ == '__main__':
    unittest.main()
