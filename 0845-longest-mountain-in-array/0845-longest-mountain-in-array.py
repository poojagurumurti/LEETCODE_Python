class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
    
        longest = 0
        i = 1  # Start from the second element
    
        while i < n - 1:
        # Check if arr[i] is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i - 1
                right = i + 1
            
            # Expand leftwards
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
            
            # Expand rightwards
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
            
            # Calculate mountain length
                longest = max(longest, right - left + 1)
            
            # Move i to the right end of the current mountain
                i = right
            else:
                i += 1
    
        return longest
        