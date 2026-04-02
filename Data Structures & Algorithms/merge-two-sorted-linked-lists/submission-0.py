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
        
        head_new = None
        tail_new = None

        while list1 and list2:
            if list1.val < list2.val:
                if not head_new and not tail_new:
                    head_new = list1
                    tail_new = list1
                    list1 = list1.next                   
                else:
                    tail_new.next = list1
                    tail_new = tail_new.next
                    list1 = list1.next
            else:
                if not head_new and not tail_new:
                    head_new = list2
                    tail_new = list2
                    list2 = list2.next
                else:
                    tail_new.next = list2
                    tail_new = tail_new.next
                    list2 = list2.next

        if list1:
            tail_new.next = list1
        else:
            tail_new.next = list2
        return head_new