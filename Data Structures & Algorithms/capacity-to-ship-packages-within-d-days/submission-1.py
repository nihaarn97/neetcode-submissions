class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        weightSum = sum(weights)
        maxWeight = max(weights)
        minWeight = 0
        l = 0
        r = weightSum
        while l<=r:
            mid = (l+r)//2
            if mid < maxWeight:
                l = mid+1
                continue
            else:
                cursum = 0
                count = 0
                for val in weights:
                    if cursum+val<=mid:
                        cursum += val
                    else:
                        cursum = val
                        count = count+1 
                
                count = count+1

                if count<=days:
                    minWeight = mid
                    r = mid - 1
                else:
                    l = mid+1

        return minWeight
        