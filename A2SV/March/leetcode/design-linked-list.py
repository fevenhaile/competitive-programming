class MyLinkedList:
    def __init__(self):
        self.head = None
    def get(self, index: int) -> int:
        i = 0
        temp = self.head
        while temp:
            if i == index:
                return temp.val
            temp = temp.next
            i+=1
        return -1

    def addAtHead(self, val: int) -> None:
        curr = Node(val)
        curr.next = self.head
        self.head = curr
        print(self.head.val)

    def addAtTail(self, val: int) -> None:
        curr = Node(val)
        if self.head is None:
            self.head = curr
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = curr
    def addAtIndex(self, index: int, val: int) -> None:
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        if index == 0:
            self.addAtHead(val)
        elif count == index:
            self.addAtTail(val)
        else:
            curr = Node(val)
            temp  = self.head
            i = 0
            while temp and temp.next:
                if i == index - 1:
                    x = temp.next
                    temp.next = curr
                    curr.next = x
                temp  = temp.next
                i += 1

        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
        else:
            temp =self. head
            i = 0
            while temp and temp.next:
                if i == index - 1:
                    temp.next = temp.next.next
                
                temp = temp.next
                i += 1
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None