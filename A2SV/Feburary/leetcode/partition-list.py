# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessthan1 = ListNode()
        lessthan = lessthan1
        greaterthan1 = ListNode()
        greaterthan = greaterthan1
        pointer = head
        while pointer:
            if pointer.val < x:
                lessthan.next = pointer
                lessthan = lessthan.next
            else:
                greaterthan.next = pointer
                greaterthan = greaterthan.next

            pointer = pointer.next
        lessthan.next = greaterthan1.next
        greaterthan.next = None
        return lessthan1.next

