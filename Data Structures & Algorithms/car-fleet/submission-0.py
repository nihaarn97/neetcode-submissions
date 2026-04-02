class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        steps_needed = [(pos, (target - pos)/speed) for pos, speed in zip(position, speed)]
        steps_needed.sort(key = lambda x: x[0])
        for val in steps_needed:
            if not stack:
                stack.append(val)
            else:
                while stack:
                    if val[1] >= stack[-1][1]:
                        stack.pop()
                    else:
                        break
                stack.append(val)
        
        return len(stack)