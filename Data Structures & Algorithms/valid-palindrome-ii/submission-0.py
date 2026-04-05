class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(sentence):
            left, right = 0, len(sentence) - 1
            while left<right:
                if sentence[left] != sentence[right]:
                    return False
                left += 1
                right -= 1
            return True
        left, right, used = 0, len(s) - 1, False
        while left<right:
            if s[left] != s[right]:
                if used:
                    return False
                used = True
                return helper(s[left:right]) or helper(s[left+1:right+1])
            left+= 1
            right -= 1
        return True