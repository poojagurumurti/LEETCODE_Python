class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count ={0:1}
        current_sum, count=0,0
        for num in nums:
            current_sum += num  # Update prefix sum

            # Check if (current_sum - k) exists in the dictionary
            if (current_sum - k) in prefix_sum_count:
                count += prefix_sum_count[current_sum - k]

            # Update prefix sum count in the dictionary
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

        return count



