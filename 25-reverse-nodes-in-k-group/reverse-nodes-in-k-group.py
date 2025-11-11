# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        def rev(curr,end):
            prev=None
            while curr!=end:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        tail=head
        for _ in range(k):
            if tail == None:
               return head
            tail=tail.next
        new_head=rev(head,tail)
        head.next=self.reverseKGroup(tail,k)
        return new_head
       