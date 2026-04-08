class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = [-1]
        for num in arr[:0:-1]:
            max_right.append(max(num, max_right[-1]))
        arr = list(reversed(max_right))
        return arr