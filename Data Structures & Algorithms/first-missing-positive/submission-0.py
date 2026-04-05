class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        from collections import defaultdict
        n = len(nums)
        seen = defaultdict(int)

        for num in nums:
            seen[num] = 1
        
        ans = 0
        while True:
            ans += 1
            if not seen[ans]:
                return ans
            