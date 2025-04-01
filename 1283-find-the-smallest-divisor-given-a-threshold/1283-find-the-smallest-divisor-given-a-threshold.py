class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        def canDivide(k):
            total = 0
            for num in nums:
                total+=ceil(num/k)
            return total<=threshold
        while left<=right:
            mid = (left+right)//2
            if canDivide(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left 
        