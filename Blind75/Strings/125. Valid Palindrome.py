class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Two-pointer approach ignoring non-alphanumeric chars and case.
        i,j = 0,len(s)-1
        while i < j :
            # advance i to next alnum or past j 
            while i < j and not s[i].isalnum():
                i+=1
            # move j to previous alnum or before i
            while i < j and not s[j].isalnum():
                j-=1
            # compare lowercase characters
            if(s[i].lower()!=s[j].lower()):
                return False
            i+=1
            j-=1
        return True
