# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # def revll(self,head):
        #     curr=head
        #     prev=None
        #     while curr != None:
        #         temp=curr.next
        #         curr.next=prev
        #         prev=curr
        #         curr=temp
        #     return head
        # curr1=self.revll(l1)
        # curr2=self.revll(l2)
        curr1=l1
        curr2=l2
        totnode=ListNode(0)
        res=totnode
        sum=0
        carry=0
        while curr1 != None or curr2 != None or carry !=0:
            if curr1:
                vall1=curr1.val
            else:
                vall1=0
            if curr2:
                vall2=curr2.val
            else:
                vall2=0
            sum=vall1+vall2+carry
            num=sum%10
            carry=sum//10
            totnode.next=ListNode(num)
            totnode=totnode.next
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
        return res.next