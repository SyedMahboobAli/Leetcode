class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Hashmap solution. Other solution is using Hashset
        last_seen = {}
        l=0
        max_length = 0

        for r in range(len(s)):
            if s[r] in last_seen:
                l = max(last_seen[s[r]]+1,l) ## Move left pointer past the duplicate. And if we don't use max here, we might move the l backwards, and we might end up getting duplicates because current comparison is with only curr character
            last_seen[s[r]] = r
            max_length = max(max_length,r-l+1) #r-l+1 coz index starts at 0
        
        return max_length
