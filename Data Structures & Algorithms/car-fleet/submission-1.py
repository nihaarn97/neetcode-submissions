class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        steps = []
        stack = []
        for idx, val in enumerate(position):
            time = (target - position[idx])/speed[idx]
            steps.append((position[idx], time))

        steps = sorted(steps, key=lambda x: x[0])
        print(steps)
        for val in steps:
            if stack:
                while stack:
                    if stack[-1][1] > val[1]:
                        break
                    else:
                        stack.pop()
            stack.append(val)

        return len(stack)
        