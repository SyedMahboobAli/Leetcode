class Solution {
    public int maxArea(int[] height) {
        int max_water = 0;
        int l = 0, r = height.length - 1;
        while (l < r) {
            int water = (r - l) * Math.min(height[l], height[r]);
            max_water = Math.max(max_water, water);
            if (height[l] < height[r]) {
                l++;
            } else
                r--;
        }
        return max_water;
    }
}
