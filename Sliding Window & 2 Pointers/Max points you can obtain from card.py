# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum=sum(cardPoints[:k])
        right_sum=0
        max_score=left_sum
        for i in range(k):
            left_sum-=cardPoints[k-i-1]
            right_sum+=cardPoints[len(cardPoints)-i-1]
            max_score=max(max_score,left_sum+right_sum)
        return max_score




        