class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        results = set()
        for val in emails:
            parts = val.split('@')
            res = ""
            for ch in parts[0]:
                if ch == ".":
                    continue
                elif ch == "+":
                    break
                else:
                    res = res + ch
            results.add(res+parts[1])

        return len(results)

        