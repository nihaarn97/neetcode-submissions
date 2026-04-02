# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        new_head = None
        new_curr = None
        curr1 = list1
        curr2 = list2
        while curr1!= None and curr2!=None:
            if curr1.val <= curr2.val:
                if not new_head:
                    new_head = curr1
                    new_curr = curr1
                    curr1 = curr1.next
                else:
                    new_curr.next = curr1
                    new_curr = new_curr.next
                    curr1 = curr1.next

            else:
                if not new_head:
                    new_head = curr2
                    new_curr = curr2
                    curr2 = curr2.next
                else:
                    new_curr.next = curr2
                    new_curr = new_curr.next
                    curr2 = curr2.next
        
        while curr1!=None:
            new_curr.next = curr1
            new_curr = new_curr.next
            curr1 = curr1.next

        while curr2!=None:
            new_curr.next = curr2
            new_curr = new_curr.next
            curr2 = curr2.next
        
        return new_head
