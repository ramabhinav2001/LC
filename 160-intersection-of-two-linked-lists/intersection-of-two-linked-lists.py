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
        countA=0
        countB=0
        while currA:
            currA=currA.next
            countA +=1
        while currB:
            currB=currB.next
            countB +=1
        currA=headA
        currB=headB
        if countA>countB:
            diff=countA-countB
            if  diff!=0:
                for _ in range(diff):
                    currA=currA.next
                
        else:
            diff=countB-countA
            if  diff!=0:
                for _ in range(diff):
                    currB=currB.next
        while currA!=currB:
            currA=currA.next
            currB=currB.next
        return currA
            
