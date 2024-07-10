# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution(object):
    def maxScore(self, cardPoints, k):
        l_sum=0
        max_sum=0
        for i in range(k):
            l_sum+=cardPoints[i]
        max_sum=l_sum

        r_sum=0
        r_index=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            l_sum-=cardPoints[i] #taking out from left_Sum one by one 
            r_sum+=cardPoints[r_index]
            r_index-=1

            max_sum=max(max_sum,(l_sum+r_sum))
        return max_sum




        