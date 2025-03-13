class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_length =0
        n = len(nums)
        for num in nums:
            if num == 1:
                count +=1
                max_length = max(count,max_length)
            else:
                count =0
        return max_length
        