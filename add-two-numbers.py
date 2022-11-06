# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        head=res
        carry=0
        while(l1 or l2 or carry):
            
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            
            if carry>=10:
                value=carry%10
                carry//=10
            else:
                value=carry
                carry=0
            res.next=ListNode(value)
            res=res.next
        return head.next
