class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for val in asteroids:
            if not stack:
                stack.append(val)
            elif (val<0 and stack[-1]<0) or (val>0 and stack[-1]>0) or (stack[-1]<0 and val>0):
                stack.append(val)
            else:
                flag = 0
                while stack:
                    if stack[-1] > abs(val):
                        flag = 1
                        break
                    elif stack[-1] == abs(val):
                        stack.pop()
                        flag = 1
                        break
                    elif stack[-1] < 0:
                        break
                    else:
                        stack.pop()

                if flag == 0:
                    stack.append(val)

        return stack



        