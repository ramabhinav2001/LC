# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or head.next == None:
            return None
        slow=head
        fast=head
        prev=None

        while fast != None and fast.next !=None:
            prev=slow
            slow=slow.next
            fast=fast.next.next

        if prev:
            prev.next=slow.next
        
        return head


        
        