# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        tail=head
        length=1
        while tail.next != None:
            length +=1
            tail=tail.next
        pos=k % length
        if pos == 0:
            return head
        curr=head
        for _ in range(length-pos-1):
            curr=curr.next
        new_head=curr.next
        curr.next=None
        tail.next=head
        return new_head

            

            