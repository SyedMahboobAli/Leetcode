class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    private List<Integer> subset = new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {
        boolean[] used = new boolean[nums.length];
        backtrack(nums,used);
        return res;
    }

    private void backtrack(int[] nums, boolean[] used){
        if(subset.size() == nums.length){
            res.add(new ArrayList<>(subset));
        }

        for(int i =0;i<nums.length;i++){
            if(used[i]) continue;

            used[i] = true;
            subset.add(nums[i]);

            backtrack(nums,used);

            subset.remove(subset.size() - 1);
            used[i] = false;
        }
    }
}
