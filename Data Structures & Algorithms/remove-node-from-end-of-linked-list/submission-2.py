# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count = count+1
            curr = curr.next

        
        iterations = count - n - 1
        print(iterations)

        if iterations == -1:
            return head.next
        else:
            curr = head
            i = 0
            while i < iterations:
                curr = curr.next
                i = i+1
            curr.next = curr.next.next
            return head
            

