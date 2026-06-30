class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    private List<Integer> subset = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        backtrack(0,nums);
        return res;
    }

    private void backtrack(int start, int[] nums){
        
        //every path is a valid path
        res.add(new ArrayList<>(subset)); // this will store a copy of subset like subset[:]

        for(int i = start;i<nums.length;i++){
            subset.add(nums[i]);
            backtrack(i+1,nums);
            subset.remove(subset.size() - 1);//this uses index and we are removing last element
        }
    }
}
