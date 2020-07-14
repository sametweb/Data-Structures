Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list?
   `O(n)`
2. What is the runtime complexity of `push` using a linked list?
   `O(1)`
3. What is the runtime complexity of `pop` using a list?
   `O(n)`
4. What is the runtime complexity of `pop` using a linked list?
   `O(1)`
5. What is the runtime complexity of `len` using a list?
   `O(1)`
6. What is the runtime complexity of `len` using a linked list?
   `O(n)`

## Queue

1. What is the runtime complexity of `enqueue` using a list?
   `O(n)`
2. What is the runtime complexity of `enqueue` using a linked list?
   `O(1)`
3. What is the runtime complexity of `dequeue` using a list?
   `O(n)`
4. What is the runtime complexity of `dequeue` using a linked list?
   `O(1)`
5. What is the runtime complexity of `len` using a list?
   `O(1)`
6. What is the runtime complexity of `len` using a linked list?
   `O(n)`

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
   `O(1)`
2. What is the runtime complexity of `ListNode.insert_before`?
   `O(1)`
3. What is the runtime complexity of `ListNode.delete`?
   `O(1)`
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
   `O(1)`
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
   `O(1)`
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
   `O(1)`
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
   `O(1)`
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
   `O(1)`
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
   `O(1)`
10. What is the runtime complexity of `DoublyLinkedList.delete`?
    `O(1)`
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    - `Array.splice:` Accepts two arguments. First one; starting index. Second one; count of items to be deleted. After the deletion, rest of the items' indexes are updated.
    - `DLL's delete:` Accepts one argument: Node to be deleted. Finds the node, update previous and next item's prev and next values and remove all pointers to the passed argument node.
    - `Comparison:`
      - In aworst case scenario, if array's first element (index 0) is deleted with splice, all the remaining items in the array will be shifted, meaning their indexes will be updated. This operation is as big as the array's size. If the array has 10000 items, all of those items have to be shifted. That's why, it is `O(n)` linear complexity.
      - However, DLL's delete method receives the node to be deleted as argument already, meaning it has access to the previous and next nodes. In a worst case scenario, `delete` updates `prev` and `next` properties of 2 nodes consecutively: `node.next` and `node.prev`. Since this is independent from the size of the DLL, it is `O(1)` constant complexity.

## Binary Search Tree

1. What is the runtime complexity of `insert`?

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`?

4. What is the runtime complexity of `for_each`?

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
