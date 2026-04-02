class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        total = n
        for idx, val in enumerate(flowerbed):
            if idx == 0 and len(flowerbed)>1:
                if flowerbed[idx+1] == 0 and flowerbed[idx]==0:
                    flowerbed[idx] = 1
                    total = total-1
            elif idx == len(flowerbed)-1:
                if flowerbed[idx-1] == 0 and flowerbed[idx]==0:
                    flowerbed[idx] = 1
                    total = total-1
            elif flowerbed[idx-1] == 0 and flowerbed[idx+1] == 0:
                if flowerbed[idx] == 0:
                    flowerbed[idx] = 1
                    total = total-1
            if total==0:
                return True
            
        if total==0:
            return True
        return False
                
        