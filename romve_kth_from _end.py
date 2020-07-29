'''
Write a function that receives as input the head node of a linked list and an integer k. Your function should remove the kth node from the end of the linked list and return the head node of the updated list.

For example, if we have the following linked list: 
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (14) -> (13) -> (12) -> (11) -> null

The head node would refer to the node (20).  Let k = 4, so our function should remove the 4th node from the end of the linked list, the node (14).

After the function executes, the state of the linked list should be:
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (13) -> (12) -> (11) -> null

If k is longer than the length of the linked list, the linked list should not be changed.

Can you implement a solution that performs a single pass through the linked list and doesn't use any extra space?

Note: When reading the tests, the linked list contents are enumerated in between square brackets; this does NOT mean the inputs are arrays.

For example, a test input of head: [2, 4 ,6] indicates that the input is a singly-linked list
(2) -> (4) -> (6) -> null whose head is the first element in the linked list.

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer head

[input] integer k

[output] linkedlist.integer
'''


def remove_kth_from_end(head, k):
    curr = head
    length = 0
# find the length of the linked list
    while curr is not None:
        curr = curr.next
        length += 1
# find index j that from the head of the list
    j = length - k

    if k > length or k == 0:
        return head
# find proper node to remove
    prev = None
    pointer = head
    while j != 0:
        prev = pointer
        pointer = pointer.next
        j -= 1
# remove node
    if prev is None:
        return head.next
    else:
        prev.next = pointer.next
        pointer.next = None
        return head
