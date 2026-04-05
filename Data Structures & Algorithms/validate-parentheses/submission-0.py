class Solution:
    def isValid(self, s: str) -> bool:
        left_chars = []
        lookup = { "(" : ")", "[" : "]", "{" : "}"}
        for c in s:
            if c in lookup:
                left_chars.append(c)
            else:
                if len(left_chars) < 1:
                    return False
                top = left_chars.pop()
                if lookup[top] != c:
                    return False
        return not left_chars