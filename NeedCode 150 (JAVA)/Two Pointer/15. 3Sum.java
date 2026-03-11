class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        ArrayList<List<Integer>> triplets = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] > 0)
                break;

            if (i > 0 && nums[i - 1] == nums[i])
                continue;

            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];

                if (sum < 0) {
                    l++;
                } else if (sum > 0) {
                    r--;
                } else {
                    triplets.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++;
                    r--;

                    while (l < r && nums[l - 1] == nums[l])
                        l++;
                    while (l < r && nums[r] == nums[r + 1])
                        r--;
                }
            }
        }
        return triplets;
    }
}
