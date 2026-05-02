class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1;
        int r = 0;
        
        // find max pile
        for (int p : piles) {
            r = Math.max(r, p);
        }
        
        int ans = r;
        
        while (l <= r) {
            int mid = l + (r - l) / 2;
            
            long hours = 0; // IMPORTANT: use long
            
            for (int p : piles) {
                // ceil(p / mid)
                hours += (p + (long)mid - 1) / mid;
            }
            
            if (hours <= h) {
                ans = mid;
                r = mid - 1; // try smaller speed
            } else {
                l = mid + 1; // need more speed
            }
        }
        
        return ans;
    }
}
