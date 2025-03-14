class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # To count cases where exactly k odds start from index 0
    
        odd_count = 0  # Prefix sum (number of odd numbers seen so far)
        result = 0
    
        for num in nums:
            if num % 2 == 1:  # Odd number contributes +1 to the prefix sum
                odd_count += 1
        
            # If we have seen (odd_count - k), it means a valid subarray exists
            result += prefix_count[odd_count - k]
        
            # Update frequency of current prefix sum
            prefix_count[odd_count] += 1
    
        return result

       
    