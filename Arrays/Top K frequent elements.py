# updated new
# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Create a dictionary to count frequencies
        frequency_dict = {}
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        # Step 2: Sort the elements based on frequency
        # Sort by values (frequencies) in descending order and keep the top k keys
        sorted_elements = sorted(frequency_dict, key=lambda x: frequency_dict[x], reverse=True)
        
        # Step 3: Return the top k frequent elements
        return sorted_elements[:k]
