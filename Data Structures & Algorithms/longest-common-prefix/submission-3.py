class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = 0
        if len(strs) == 1:
            return strs[0]
        while True:
            for i in range(1, len(strs)):
                if min(len(strs[i]), len(strs[i-1]))<length + 1 or strs[i][length] != strs[i-1][length]:
                    return strs[0][:length]
            length += 1
        return strs[0][:length]