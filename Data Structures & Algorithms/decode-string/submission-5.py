class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        curr_str = ""
        curr_num = 0
        for char in s:
            if char == "[":
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_str = ""
                curr_num = 0
            elif char == "]":
                # tmp = curr_str
                # curr_str = str_stack.pop()
                # count = num_stack.pop()
                # curr_str += tmp * count
                curr_str = str_stack.pop() + (num_stack.pop()*curr_str)
            elif char.isdigit():
                curr_num = curr_num*10 + int(char)
            else:
                curr_str += char
        
        return curr_str