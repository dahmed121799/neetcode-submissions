class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        current = self.head

        for i in range(index):
            current = current.next

        return current.val    

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

        if self.tail is None:
            self.tail = newNode

        self.size += 1    

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1         

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False

        if index == 0:
            self.head = self.head.next
            self.size -= 1

            if self.size == 0:
                self.tail = None

            return True        

        current = self.head

        for i in range(index - 1):
            current = current.next
            
        current.next = current.next.next

        if index == self.size - 1:
            self.tail = current

        self.size -= 1
        return True    
        

    def getValues(self) -> List[int]:
        myList = []
        current = self.head

        for i in range(self.size):
            myList.append(current.val)
            current = current.next

        return myList