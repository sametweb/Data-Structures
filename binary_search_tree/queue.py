"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from singly_linked_list import Node, LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        return self.storage.tail.get_value()

    def dequeue(self):
        if self.size == 0:
            return
        self.size -= 1
        return self.storage.remove_head()

        # # Array solution
        # class Queue:
        #     def __init__(self):
        #         self.size = 0
        #         self.storage = []

        #     def __len__(self):
        #         return len(self.storage)

        #     def enqueue(self, value):
        #         self.storage.append(value)
        #         self.size = len(self.storage)

        #     def dequeue(self):
        #         if len(self.storage) == 0:
        #             return None

        #         dequeued = self.storage[0]

        #         for i in range(len(self.storage)):
        #             if i != 0:
        #                 self.storage[i - 1] = self.storage[i]
        #         self.storage.remove(self.storage[len(self.storage) - 1])
        #         self.size = len(self.storage)
        #         return dequeued

        # # End of Array solution
