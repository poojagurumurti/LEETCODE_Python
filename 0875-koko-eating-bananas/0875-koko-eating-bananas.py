class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(piles,k ,h):
            time =0
            for pile in piles:
                time += (pile + k - 1) // k
            return time <=h 
        
        low , high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if canEat(piles,mid,h):
                high = mid
            else:
                low = mid+1
        return low



       


        