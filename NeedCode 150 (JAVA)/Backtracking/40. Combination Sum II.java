class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    private List<Integer> subset =  new ArrayList<>();

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        backtrack(0,candidates,target);
        return res;
    }

    private void backtrack(int start, int[] candidates, int target){
        if(target == 0){
            res.add(new ArrayList<>(subset));
        }

        for(int i = start;i<candidates.length;i++){
            if(i > start && candidates[i-1] == candidates[i]) continue;
            if(candidates[i] > target) break;

            subset.add(candidates[i]);
            backtrack(i+1,candidates,target - candidates[i]); // now we are using i + 1 to avoid using same number again. Each number can be used only once
            subset.remove(subset.size() - 1);
        }
    }
}
