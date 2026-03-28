class Solution {
    public String minWindow(String s, String t) {
        if (t.length() > s.length()) return "";

        int [] count = new int[128]; //ASCII
        for(char c:t.toCharArray()){
            count[c]++;
        }
        int left = 0, right = 0;
        int required = t.length(); // total chars required
        int minLen = Integer.MAX_VALUE;
        int start = 0;
        
        while(right < s.length()){
            char rChar = s.charAt(right);

            //if char needed, decrease required
            if(count[rChar] > 0) required--;
            count[rChar]--;
            right++;
            //While all char matched
            while(required == 0){
                if(right -left < minLen){
                    minLen = right-left;
                    start = left;
                }
                char lChar = s.charAt(left);
                count[lChar]++;
                //if removing breaks validity
                if(count[lChar] > 0){
                    required++;
                }
                left++;

            }
        }
        return minLen == Integer.MAX_VALUE ? "" : s.substring(start,start+minLen);
    }
}
