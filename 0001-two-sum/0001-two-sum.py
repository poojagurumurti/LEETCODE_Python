# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         pair_idx = {}

#         for i, num in enumerate(nums):
#             if target - num in pair_idx:
#                 return [i, pair_idx[target - num]]
#             pair_idx[num] = i
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}  # Dictionary to store numbers and their indices
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the number needed to reach the target sum
            if complement in pair_idx:  # Check if the complement exists in the dictionary
                return [pair_idx[complement], i]  # Return the indices of the complement and current number
            pair_idx[num] = i  # Store the current number with its index

