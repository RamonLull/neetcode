class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            count = 1
            current = 0

            for num in nums:
                if current + num <= max_sum:
                    current += num
                else:
                    count += 1
                    current = num

            return count <= k

        left, right = max(nums), sum(nums)
        ans = float('inf')
        while left <= right:
            mid = (left + right) // 2

            if can_split(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans