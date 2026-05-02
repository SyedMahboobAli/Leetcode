class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;

        int pivot = findPivot(nums);

        if(target >= nums[pivot] && target <= nums[n-1])
            return binarySearch(nums,pivot,n-1,target);
        else
            return binarySearch(nums,0,pivot-1,target);
    }

    private int findPivot(int[] nums){
        int l=0, r= nums.length -1;

        while(l<r){
            int mid = l + (r-l)/2;
            if(nums[mid] > nums[r])
                l = mid +1;
            else
                r = mid;
        }
        return l;
    } 

    private int binarySearch(int[] nums,int l, int r, int target){
        while(l<=r){
            int mid = l+(r-l)/2;
            if (nums[mid] == target){
                return mid;
            }
            if (nums[mid] > target)
                r = mid -1;
            else
                l = mid +1;
        }
        return -1;
    }
}
