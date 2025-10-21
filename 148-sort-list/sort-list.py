# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None:
            return head
        prev=None
        fast=head
        slow=head
        while fast !=None and fast.next != None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        l1=self.sortList(head)
        l2=self.sortList(slow)

        return self.merge(l1,l2)

    def merge(self,l1,l2):
        l=ListNode(0)
        x=l
        while l1 != None and l2 != None:
            if l1.val<l2.val:
                x.next=l1
                l1=l1.next
            else:
                x.next=l2
                l2=l2.next
            x=x.next
        if l1 != None:
            x.next=l1
        if(l2 != None):
            x.next=l2
        return l.next


