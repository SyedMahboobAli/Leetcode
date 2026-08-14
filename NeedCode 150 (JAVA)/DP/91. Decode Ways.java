class Solution {
    public int numDecodings(String s) {
        int n = s.length();

        if(n == 0)
            return 0;
        
        int prev2 = 1; //base case
        int prev1;
        if(Integer.parseInt(s.substring(0,1)) == 0 ) // or s.charAt(0) == '0'
            prev1 = 0;
        else
            prev1 = 1;
        
        for(int i = 2;i<=n;i++){ //we are always creating substring until i, so i is not included. so we are going until n+1
            int oneDigit = Integer.parseInt(s.substring(i-1,i));
            //or int oneDigit = s.charAt(i - 1) - '0';
            int twoDigit = Integer.parseInt(s.substring(i-2,i));
            //or int twoDigit = (s.charAt(i - 2) - '0') * 10 + (s.charAt(i - 1) - '0');

            int curr = 0;

            if(oneDigit>=1 && oneDigit<=9)
                curr += prev1;

            if(twoDigit >=10 && twoDigit<=26)
                curr += prev2;
            
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
}
