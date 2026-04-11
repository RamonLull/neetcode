class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s) - 1
        while idx >= 0 and not s[idx].isalpha():
            idx -= 1
        end_of_word = idx
        while idx >= 0 and s[idx].isalpha():
            idx -= 1
        return end_of_word - idx 