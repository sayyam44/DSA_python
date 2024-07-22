# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
#given the coins should be in sorted order and no 2 consecutive coins sum
#should be greater than the 3rd coin value 
class Solution(object):
    def coinChange(self, coins, amount):
        cnt = 0
        # Iterate over the coins array in reverse order
        for i in range(len(coins) - 1, -1, -1):
            while amount >= coins[i]:
                amount -= coins[i]
                cnt += 1
        
        # If there is still an amount left, return -1 indicating it cannot be formed
        if amount != 0:
            return -1
        
        return cnt

# Example usage:
coins = [2, 5, 10, 1]
amount = 27
sol = Solution()
print(sol.coinChange(coins, amount))  # Output: 27
