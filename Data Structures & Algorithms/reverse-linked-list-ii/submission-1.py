# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        temp = []
        curr = head
        while curr:
            temp.append(curr)
            curr = curr.next

        i = left - 1
        j = right - 1

        while i<=j:
            temp[i], temp[j] = temp[j], temp[i]
            i = i+1
            j = j-1

        for i in range(len(temp)-1):
            temp[i].next = temp[i+1]

        temp[-1].next = None

        return temp[0]

            