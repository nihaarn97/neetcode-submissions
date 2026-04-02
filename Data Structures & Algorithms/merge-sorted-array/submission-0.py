class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        l1 = 0
        l2 = 0
        while l1<m and l2<n:
            if nums1[l1]<nums2[l2]:
                res.append(nums1[l1])
                l1+=1
            else:
                res.append(nums2[l2])
                l2+=1

        if l1<m:
            while l1<m:
                res.append(nums1[l1])
                l1+=1
        elif l2<n:
            while l2<n:
                res.append(nums2[l2])
                l2+=1

        i = 0
        while i<len(nums1):
            nums1[i] = res[i]
            i+=1 
        