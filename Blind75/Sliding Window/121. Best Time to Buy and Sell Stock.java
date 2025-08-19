class Solution {
    public int maxProfit(int[] prices) {
        int min=0;
        int maxp=0;
        int p=0;
        for(int i=1; i<prices.length;i++){
            if(prices[min]<prices[i]){
                p=prices[i]-prices[min];
                if(maxp<p)
                maxp=p;
            }
            else
            min=i;
        }
        return maxp;
    }
}
}
