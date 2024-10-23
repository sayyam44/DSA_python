# https://leetcode.com/problems/group-anagrams/
from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            # Create a count of characters for each string
            count = [0] * 26  # For each letter in the alphabet
            
            # Increment the count for each character in the string
            for j in s:
                count[ord(j) - ord('a')] += 1
            
            # Use the tuple of counts as the key and append the string to the list
            dic[tuple(count)].append(s)
        
        # Convert the result to a list of lists
        return list(dic.values())
