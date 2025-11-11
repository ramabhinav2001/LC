# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth_node(start, k):
            while start and k > 0:
                start = start.next
                k -= 1
            return start

        new_head = None
        prev_group_end = None
        curr = head

        while curr:
            kth_node = get_kth_node(curr, k - 1)  
            if not kth_node:
                break

            group_next = kth_node.next

            prev, node = group_next, curr
            while node != group_next:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt

            if not new_head:
                new_head = kth_node

            if prev_group_end:
                prev_group_end.next = kth_node

            prev_group_end = curr
            curr = group_next

        return new_head if new_head else head
            
        


       