class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False      # it means all elements in nums are distinct
        else:
            return True       # Duplicates found


        
        