class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0, l = 0, r = 1;
        while (r < prices.length) {
            if (prices[r] > prices[l]) {
                max_profit = Math.max(max_profit, prices[r] - prices[l]);
                r++;
            } else {
                l = r;
                r++;
            }
        }
        return max_profit;
    }
}
