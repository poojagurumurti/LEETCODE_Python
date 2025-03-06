from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1  # Fix: Correct index for `high`
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:  # Fix: Compare the value, not index
                return mid

            # Left part is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right part is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1  # Target not found
