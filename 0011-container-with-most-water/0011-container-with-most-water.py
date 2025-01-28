class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right=0,len(height) - 1
        maxi = float('-inf')
        while left < right :
            a = min(height[left],height[right])
            b = right - left
            maxi = max(maxi, a*b)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return maxi
