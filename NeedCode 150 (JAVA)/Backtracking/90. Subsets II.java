class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    private List<Integer> subset = new ArrayList<>();
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        backtrack(0,nums);
        return res;
    }

    private void backtrack(int start, int[] nums){
        //every path is valid path
        res.add(new ArrayList<>(subset));

        for(int i = start;i<nums.length;i++){
            //skip duplicates at same recursion level
            if(i>start && nums[i] == nums[i-1]) continue;

            subset.add(nums[i]);
            backtrack(i+1,nums);
            subset.remove(subset.size() -1 );

        }
    }
}
