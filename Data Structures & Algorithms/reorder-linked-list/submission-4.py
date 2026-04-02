# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr!=None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr

        curr1 = head
        curr2 = prev
        new_head = None
        new_curr = None

        while curr1 and curr2:
            if not new_head:
                new_head = curr1
                new_curr = curr1
                curr1 = curr1.next
                new_curr.next = curr2
                curr2 = curr2.next
                new_curr = new_curr.next
            else:
                new_curr.next = curr1
                curr1 = curr1.next
                new_curr = new_curr.next
                new_curr.next = curr2
                curr2 = curr2.next
                new_curr = new_curr.next

        while curr1:
            new_curr.next = curr1
            curr1 = curr1.next
            new_curr = new_curr.next

        
        