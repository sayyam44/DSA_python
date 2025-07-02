# updated new
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#optimized solution - tc=n,sc=1
#Updated

#In this ques we are finding the point og min price till now and selling it on every price and 
#thus calculating the profit and max_profit on each and every day.
def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price #profit = sell on current day - min price till now
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


    




        
