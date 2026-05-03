class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length)
            return findMedianSortedArrays(nums2, nums1);

        int m = nums1.length;
        int n = nums2.length;
        int l = 0, r = m;
        int total_left = (m + n + 1) / 2;

        while (l <= r) {
            int mid1 = (l + r) / 2;
            int mid2 = total_left - mid1;

            int left1 = (mid1 == 0) ? Integer.MIN_VALUE : nums1[mid1 - 1];
            int right1 = (mid1 == m) ? Integer.MAX_VALUE : nums1[mid1];

            int left2 = (mid2 == 0) ? Integer.MIN_VALUE : nums2[mid2 - 1];
            int right2 = (mid2 == n) ? Integer.MAX_VALUE : nums2[mid2];

            if (left1 <= right2 && left2 <= right1) {
                //even
                if ((m + n) % 2 == 0) {
                    return (Math.max(left1, left2) + Math.min(right1, right2)) / 2.0;
                } else
                    return Math.max(left1, left2);
            }
            //move left
            else if (left1 > right2) {
                r = mid1 - 1;
            }
            // move right
            else {
                l = mid1 + 1;
            }

        }
        return -1;

    }
}
