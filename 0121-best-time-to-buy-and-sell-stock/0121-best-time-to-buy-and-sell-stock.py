class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize to a very high value
        max_profit = 0  # Initialize profit as 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update minimum price if a lower price is found
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max profit if the curren
        return max_profit   
        
  
        