class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int pre = 1, post = 1;
        res[0] = 1;
        for(int i=0;i<n;i++){
            res[i] = pre;
            pre *= nums[i];
        }
        for(int i = n-1;i>=0;i--){
            res[i] *= post;
            post *= nums[i];
        }
        return res;
    }
}
