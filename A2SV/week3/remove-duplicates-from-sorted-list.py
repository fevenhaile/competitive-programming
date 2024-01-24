# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        while pointer:
            x = pointer.next
            
            if x and pointer.val == x.val:
                pointer.next = x.next
            else:
                pointer = pointer.next
        return head
        