class Solution {
    private List<List<String>> res = new ArrayList<>();
    private List<String> subset = new ArrayList<>();

    public List<List<String>> partition(String s) {
        backtrack(0,s);
        return res;
    }

    //start is the index where we need to partition next.

    private void backtrack(int start, String s){
        if(start == s.length()) 
            res.add(new ArrayList<>(subset));
        
        //This loop tries every possible substring starting at start.
        for(int end = start;end<s.length();end++){
            if(isPalindrome(s,start,end)){
                subset.add(s.substring(start,end+1)); // ecause substring excludes the end index.
                backtrack(end + 1, s);
                subset.remove(subset.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String s, int l, int r){
        while(l<r){
            if(s.charAt(l) != s.charAt(r))
                return false;
            l+=1;
            r-=1;
        }

        return true;
    }

}

//The only difference is what you choose:

//Subsets: choose an element.
//Combination Sum: choose a number.
//Palindrome Partitioning: choose a palindromic substring.
