class Solution {
    public int trap(int[] height) {
        int n = height.length, l = 0, r = n - 1;
        int leftmost = height[l], rightmost = height[r];
        int water = 0;
        while (l < r) {
            if (leftmost < rightmost) {
                l++;
                leftmost = Math.max(leftmost, height[l]);
                water += leftmost - height[l];
            } else {
                r--;
                rightmost = Math.max(rightmost, height[r]);
                water += rightmost - height[r];
            }
        }
        return water;

    }
}
