# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)


        leftprev = dummy
        current = head
        for i in range(left-1):
            leftprev = current
            current = current.next
        
        prev = None
        
        
        for i in range((right - left)+1):
            if current is None:
                break
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        leftprev.next.next = current
        leftprev.next = prev

        return dummy.next



        