class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #approach 2: same but the difference is you need not handle  Counts2[s2[l]] == 0 and Counts1 and Counts2 are of fixed length and are frequency arrays and not dictionary
        n1,n2= len(s1),len(s2)
        counts1 = [0] * 26
        counts2 = [0] * 26
        l=0
        for ch in s1:
            counts1[ord(ch) - ord('a')] += 1
        for r in range(n2):
            counts2[ord(s2[r]) - ord('a')] += 1

            if (r-l+1 > n1):
                counts2[ord(s2[l]) - ord('a')] -= 1
                l+=1
            if counts1==counts2:
                return True
        return False

        # approach 1
        #In other words, check whether a substring of s2 is an anagram of s1. So we slide a window of size len(s1) over s2 and compare character frequencies.
        Counts1 = Counter(s1)
        Counts2={}
        n2 = len(s2)
        n1 = len(s1)
        l = 0
        for r in range(n2):
            Counts2[s2[r]] = Counts2.get(s2[r],0) + 1
            while(r-l+1 > n1): #since checking anagram of s1 in s2
                Counts2[s2[l]]-=1
                if Counts2[s2[l]] == 0:#else Counts2 == Counts1 will give wrong value. like for 'k' : 0 the count can be zero
                    del Counts2[s2[l]]
                l+=1
            if(Counts2 == Counts1):
                return True   
        return False

        
