class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0 # Left pointer
        max_length=0 #float('-inf') not needed as "" is zero
        char_set = set() # To store current window characters

        for right in range(len(s)):  # Right pointer moves forward
            if(s[right] in char_set): # If duplicate found
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left+=1
            char_set.add(s[right]) # Add current character
            max_length=max(max_length,right-left+1) # or max_length=max(max_length,len(char_set))
        
        return max_length

        #approach 2: use dictionary

        mp = {} # Stores last seen index of each character
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l) # Move left pointer past the duplicate. And if we don't use max here, we might move the l backwards, and we might end up getting duplicates because current comparison is with only curr character
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
