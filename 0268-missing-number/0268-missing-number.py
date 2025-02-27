class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len (nums)
        summation = (N *(N+1)) // 2
        s2 = sum(nums)
        difference = summation - s2
        return difference