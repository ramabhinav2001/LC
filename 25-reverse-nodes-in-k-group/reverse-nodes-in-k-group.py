# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        grp_prev=dummy

        def get_kth_node(start, k):
            while start and k>0:
                start=start.next
                k -=1
            return start
        while True:
            kth_node=get_kth_node(grp_prev,k)
            if kth_node==None:
                break
            grp_next=kth_node.next
            prev=kth_node.next
            curr=grp_prev.next
            while curr != grp_next:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=grp_prev.next
            grp_prev.next=kth_node
            grp_prev=temp
        return dummy.next

            
        


       