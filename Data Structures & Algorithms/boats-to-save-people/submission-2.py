class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        visited = set()
        boats = 0
        while l<r:
            if people[l] + people[r] <= limit:
                visited.add(l)
                visited.add(r)
                boats = boats + 1
                l = l+1
                r = r-1
            else:
                visited.add(r)
                boats = boats + 1
                r = r-1

        if l == r and l not in visited and r not in visited:
            boats = boats+1

        return boats            
        