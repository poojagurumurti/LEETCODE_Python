class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        sort = sorted(nums)
        for i in nums:
            ans.append(sort.index(i))
        return ans
        