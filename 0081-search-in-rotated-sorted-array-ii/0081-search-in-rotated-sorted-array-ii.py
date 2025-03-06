from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True  # Fix: Return boolean instead of index
            
            # If duplicates exist, shrink the search space
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue  # Fix: 'continue' is now inside the loop

            # Left part is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:  # Fix: Correct comparison
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:  # Fix: Correct comparison
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False  # Fix: Return False if the target is not found
