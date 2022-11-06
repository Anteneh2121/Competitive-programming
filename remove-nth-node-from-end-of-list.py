# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        countList = head
        count = 1

        while countList.next != None:
            count+=1
            countList = countList.next

        if count == 1:
            head = None
            return head

        countList = head
        temp = head
        i = 0

        while i<=count:
            if(i!= count-n):
                temp = countList
                countList = countList.next
                i+=1
            else:
                if temp.next != None and countList!=head:
                    temp.next = countList.next
                    break
                else:
                    head = head.next
                    return head
        return head 
