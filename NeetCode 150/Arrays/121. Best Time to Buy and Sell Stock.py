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
