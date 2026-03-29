class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result,"",0,0,n);
        return result;
    }
    public void backtrack(List<String> result, String curr,int open, int close, int n){
        if(curr.length() == 2*n){
            result.add(curr);
            return;
        }
        if (open<n){
            backtrack(result,curr+"(",open+1,close,n);
        }
        if(close<open){
            backtrack(result,curr+")",open,close+1,n);
        }

    }
}
