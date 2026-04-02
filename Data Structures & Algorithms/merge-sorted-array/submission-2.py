class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = m-1
        l2 = n-1
        i = len(nums1)-1
        while l1>-1 and l2>-1:
            if nums1[l1]>nums2[l2]:
                nums1[i] = nums1[l1]
                l1-=1
                i = i-1
            else:
                nums1[i] = nums2[l2]
                l2-=1
                i = i-1

        if l1>-1:
            while l1>-1:
                nums1[i] = nums1[l1]
                l1-=1
                i-=1
        elif l2>-1:
            while l2>-1:
                nums1[i] = nums2[l2]
                l2-=1
                i-=1 
        