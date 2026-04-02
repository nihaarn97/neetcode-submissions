import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = re.sub(r'\s\s+', ' ', s)
        s = s.lstrip()
        s = s.rstrip()
        s_list = s.split(" ")
        return len(s_list[-1])      