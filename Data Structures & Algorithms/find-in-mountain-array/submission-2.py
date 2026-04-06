class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def find_peak():
            left, right = 0, mountainArr.length() - 1
            while left < right:
                mid = (left + right) // 2
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def search(peak):
            left, right = 0, peak
            while left <= right:
                mid = (left + right) // 2
                if mountainArr.get(mid) == target:
                    return mid
                elif mountainArr.get(mid) < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        def reverse_search(peak):
            left, right = peak, mountainArr.length() - 1
            while left <= right:
                mid = (left + right) // 2
                if mountainArr.get(mid) == target:
                    return mid
                elif mountainArr.get(mid) > target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        peak = find_peak()
        left = search(peak)
        if left > -1:
            return left
        right = reverse_search(peak)
        return right