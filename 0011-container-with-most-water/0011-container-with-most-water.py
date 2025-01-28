class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1  # Step 1: Initialize pointers
        max_area = 0  # Step 2: Initialize max_area
        
        while left < right:  # Step 3: Iterate until pointers meet
            width = right - left  # Calculate the width
            current_height = min(height[left], height[right])  # Calculate the height
            max_area = max(max_area, width * current_height)  # Update max_area
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area  # Return the maximum area
