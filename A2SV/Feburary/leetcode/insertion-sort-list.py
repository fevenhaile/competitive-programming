# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        ptr = pointer
        array = []
        

        while ptr:
            array.append(ptr.val)
            ptr = ptr.next
        
        array.sort()
        
        dummy = ListNode()
        ans = dummy
        for i in range(len(array)):
            newnode = ListNode(array[i])
            dummy.next = newnode
            dummy = dummy.next
        return ans.next
        

    
         





                                                                                                                                                                                                   