# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        head = None
        curr3 = None
        carry = 0
        while curr1 and curr2:
            res = curr1.val + curr2.val + carry
            if head == None:
                if res >= 10:
                    head = ListNode(res - 10)
                    carry = 1
                else:
                    head = ListNode(res)
                curr3 = head
            else:
                if res >= 10:
                    curr3.next = ListNode(res-10)
                    carry = 1
                else:
                    curr3.next = ListNode(res)
                    carry = 0
                curr3 = curr3.next
            
            curr1 = curr1.next
            curr2 = curr2.next

        print(carry)

        while curr1:
            res = curr1.val + carry
            if res >= 10:
                curr3.next = ListNode(res-10)
                carry = 1
            else:
                curr3.next = ListNode(res)
                carry = 0
            curr3 = curr3.next
            curr1 = curr1.next

        while curr2:
            res = curr2.val + carry
            if res >= 10:
                curr3.next = ListNode(res-10)
                carry = 1
            else:
                curr3.next = ListNode(res)
                carry = 0
            curr3 = curr3.next
            curr2 = curr2.next

        if carry == 1:
            curr3.next = ListNode(1)

        return head
        