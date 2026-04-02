class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        count = 0
        while left<right:
            if people[right] == limit or people[right] + people[left]>limit:
                count = count + 1
                right = right-1

            elif people[right] + people[left] <= limit:
                count = count + 1
                right = right-1
                left = left + 1

        if left == right:
            return count+1
        
        return count

            

            
