class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        visited = set()
        l = 0
        r = len(people)-1
        boats = 0
        while l<r:
            if people[l] + people[r] <= limit:
                visited.add(l)
                visited.add(r)
                l = l+1
                r = r-1
                boats = boats + 1
            else:
                visited.add(r)
                r = r-1
                boats = boats+1

        if l==r and l not in visited:
            boats = boats+1

        return boats