class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1

        for num in nums[1:]:
            if nums[write-1] != num:
                nums[write] = num
                write += 1
        return write