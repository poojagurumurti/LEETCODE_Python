class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_range = set(range(1, len(nums)+1))
        diff = nums_range - set(nums)
        return list(diff)