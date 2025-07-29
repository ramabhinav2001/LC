# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr=head
        visited=set()
        while curr is not None:
            if curr in visited:
                return True
            visited.add(curr)
            curr=curr.next
        return False