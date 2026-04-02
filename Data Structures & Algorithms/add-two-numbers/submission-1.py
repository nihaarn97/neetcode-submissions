# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 and l2:
            val_sum = l1.val + l2.val + carry
            if val_sum >= 10:
                carry = 1
            else:
                carry = 0
            res_node = ListNode(val_sum%10)
            curr.next = res_node
            curr = res_node
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            val_sum = l1.val + carry
            if val_sum >= 10:
                carry = 1
            else:
                carry = 0
            res_node = ListNode(val_sum%10)
            curr.next = res_node
            curr = res_node
            l1 = l1.next

        while l2:
            val_sum = l2.val + carry
            if val_sum >= 10:
                carry = 1
            else:
                carry = 0
            res_node = ListNode(val_sum%10)
            curr.next = res_node
            curr = res_node
            l2 = l2.next
        
        if carry == 1:
            res_node = ListNode(1)
            curr.next = res_node
        
        return dummy.next

        