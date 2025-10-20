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
        if head.next == None:
            return head.next
        fast=head
        count=0
        while fast != None and fast.next !=None:
            fast=fast.next.next
            count +=1
        slow=head
        for _ in range(count-1):
            slow=slow.next

        temp=slow.next.next
        slow.next=temp
        return head


        
        