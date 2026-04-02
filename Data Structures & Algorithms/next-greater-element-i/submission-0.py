class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greatest = {}
        for val in nums2:
            if not stack:
                stack.append(val)
            elif val>stack[-1]:
                while stack:
                    if stack[-1]<val:
                        greatest[stack.pop()] = val
                    else:
                        break
                stack.append(val)
            else:
                stack.append(val)

        while stack:
            greatest[stack.pop()] = -1

        res = []
        for val in nums1:
            res.append(greatest[val])
        return res
