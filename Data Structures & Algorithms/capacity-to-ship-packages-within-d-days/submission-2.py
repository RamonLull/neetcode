class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calculate_days(capacity: int) -> int:
            _days = 1
            remaining = capacity
            for weight in weights:
                if weight <= remaining:
                    remaining -= weight
                else:
                    _days += 1
                    remaining = capacity - weight
            return _days
        ans = float('inf')
        left, right = max(weights), sum(weights)
        while left <= right:
            middle = (left + right) // 2
            days_needed = calculate_days(middle)
            if days_needed <= days:
                ans = middle
                right = middle - 1
            else:
                left = middle + 1
        return ans