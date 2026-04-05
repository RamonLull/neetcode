class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        BRACKET_MAP = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in BRACKET_MAP:          # Açan parantez
                stack.append(char)
            elif not stack:                   # Kapatan geldi ama stack boş
                return False
            elif BRACKET_MAP[stack.pop()] != char:  # Eşleşmiyor
                return False

        return not stack  # Stack boşsa tüm parantezler eşleşmiş