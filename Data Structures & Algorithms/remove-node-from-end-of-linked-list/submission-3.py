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

        if count-n == 0:
            head = head.next
            return head

        else:
            stop = count - n - 1
            count = 0
            curr = head
            while count<stop:
                count = count+1
                curr = curr.next

            curr.next = curr.next.next

            return head

        