# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        node=None
        while slow:
            temp=slow.next
            slow.next=node
            node=slow
            slow=temp
        first=head
        second=node
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True