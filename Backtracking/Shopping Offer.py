# updated
# https://leetcode.com/problems/shopping-offers/description/
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        # Helper function to calculate the cost of buying items directly at regular price
        def directPurchase(needs):
            return sum(needs[i] * price[i] for i in range(len(needs)))
        
        # Backtracking function to explore all possibilities
        def dfs(current_needs):
            # Start by assuming we buy everything at regular price
            min_cost = directPurchase(current_needs)
            
            # Try to use each special offer and see if it leads to a lower cost
            for offer in special:
                new_needs = current_needs[:]
                valid_offer = True
                
                # Check if this offer can be applied without exceeding the needs
                for i in range(len(needs)):
                    if new_needs[i] < offer[i]:  # Offer requires more than what we need
                        valid_offer = False
                        break
                    new_needs[i] -= offer[i]
                
                # Prune: If the offer is valid, calculate the cost after using the offer
                if valid_offer:
                    min_cost = min(min_cost, offer[-1] + dfs(new_needs))
            
            return min_cost
        
        # Start the recursion with the initial needs
        return dfs(needs)
