class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    private List<Integer> subset = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        backtrack(0,candidates,target);
        return res;
    }

    private void backtrack(int start, int[] candidates, int target){
        if(target == 0){
            res.add(new ArrayList<>(subset));
        }

        for(int i = start; i < candidates.length; i++){
            if(candidates[i] > target)
                continue;
            
            subset.add(candidates[i]);
            backtrack(i,candidates,target - candidates[i]);
            subset.remove(subset.size() - 1);

        }
    }
}
