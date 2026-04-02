class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for val in asteroids:
            if not stack:
                stack.append(val)
            elif (stack[-1]<0 and val>0) or (stack[-1]<0 and val<0) or (stack[-1]>0 and val>0):
                stack.append(val)
            else:
                flag = 0
                while stack:
                    if stack[-1]>0: 
                        if abs(stack[-1]) == abs(val):
                            stack.pop()
                            flag = 0
                            break
                        elif abs(stack[-1]) < abs(val):
                            stack.pop()
                            flag = 1
                        else:
                            flag = 0
                            break
                    else:
                        flag = 1
                        break
                if flag == 1:
                    stack.append(val)
        return stack




        