class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_duration(k: int) -> int:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours
        ans =  float('inf')
        left, right = 1, max(piles)
        while left <= right:
            middle = (left + right) // 2
            hours = calculate_duration(middle)
            if hours <= h:
                ans = middle
                right = middle -1
            else:
                left = middle + 1
        return ans