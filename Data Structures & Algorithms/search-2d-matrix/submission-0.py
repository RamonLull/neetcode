class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        row_to_be_checked = left - 1
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row_to_be_checked][mid] == target:
                return True
            elif matrix[row_to_be_checked][mid] < target:
                left += 1
            else:
                right -= 1
        return False