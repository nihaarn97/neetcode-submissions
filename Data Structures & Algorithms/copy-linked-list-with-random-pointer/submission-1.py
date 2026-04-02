"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        temp = []
        random_ptr = []
        res = []
        curr = head
        while curr:
            temp.append(curr)
            res.append(Node(curr.val))
            curr = curr.next
        
        hmap = {}

        for idx, val in enumerate(temp):
            hmap[val] = idx

        for val in temp:
            random_ptr.append(hmap.get(val.random, None))

        for i in range(len(res)-1):
            res[i].next = res[i+1]

        hmap2 = {}
        for idx, val in enumerate(res):
            hmap2[idx] = val

        for val1, val2 in zip(random_ptr, res):
            val2.random = hmap2.get(val1, None)

        return res[0]

        
        