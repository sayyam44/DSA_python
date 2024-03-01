def maxProfit(prices):
    #https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    #optimized solution - tc=n,sc=1
    #https://www.youtube.com/watch?v=eMSfBgbiEjk&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=12
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

    #brute force method 
    # value1=float('inf')
    #     for idx,val in enumerate(prices):
    #         if val<value1:
    #             value1=val
    #             index=idx
    #     if index==(len(prices)-1) or len(set(prices))==1:
    #         return 0
    #     value2=0
    #     for i in range(index+1,len(prices)):
    #         if (prices[i]>value2) and prices[i]>value1:
    #             value2=prices[i]
        
    #     return (value2-value1)

    # brute force method,tc=n2,sc=1
    # def maxProfit_my_correct_ans(self, prices: List[int]) -> int:
    #     a=min(prices)
    #     ind_a=prices.index(a)
        
    #     b=max(prices[ind_a:])
    #     return (b-a)
    




        
