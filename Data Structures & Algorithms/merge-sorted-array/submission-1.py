class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        write = 0
        for num in nums1[:m]:
            while write < len(nums2) and num>nums2[write]:
                write += 1
            nums2.insert(write, num)
            write += 1
        nums1[:] = nums2