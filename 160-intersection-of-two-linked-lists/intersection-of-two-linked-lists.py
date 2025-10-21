# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        currA=headA
        currB=headB
        while currA != currB:
            if currA == None:
                currA=headB
            else:
                currA=currA.next
            if currB == None:
                currB=headA
            else:
                currB=currB.next
        return currA