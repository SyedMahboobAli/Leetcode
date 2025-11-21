class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxp=0
        while r < len(prices):
            if(prices[l]<prices[r]):
                profit=prices[r]-prices[l]
                maxp=max(maxp,profit)
            else:
                #changing the window now. Prev window max is done
                l=r
            #at any case move r forward
            r+=1
        return maxp

#the above is a two pointer/ sliding window solution. A DP solution to this would be directly using the value in the array and not pointing the values using indexes with same logic
# DP solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy=prices[0]
        maxp=0
        for sell in prices:
            maxp=max(maxp,sell-minbuy)
            minbuy=min(minbuy,sell)
        return maxp
            
