class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True :  
            slow = nums[slow]        # To detect the cycle
            fast = nums[nums[fast]]
            if slow == fast:
                break

#  Find the duplicate (cycle entry)
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow

        



       

    

  

        
                
        