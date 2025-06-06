class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index<0 or index>=self.size:
            return -1
        current_node=self.head
        for _ in range(0, index):
            current_node=current_node.next
        return current_node.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node=ListNode(val)
        if self.head==None:
            self.head=new_node
            self.size += 1
            return
        else:
            new_node.next=self.head
            self.head=new_node
            self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        new_node = ListNode(val)
        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            current_node.next = current_node.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)