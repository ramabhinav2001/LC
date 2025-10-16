# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None or head.next== None:
            return head
        odd_n=head
        even_n=head.next
        evenH=even_n
        while even_n != None and even_n.next != None:
            odd_n.next=even_n.next
            odd_n=odd_n.next
            even_n.next=odd_n.next
            even_n=even_n.next

        odd_n.next=evenH
        return head

        



