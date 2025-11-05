class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #solution 1, TC more o(nlogn)
        return sorted(s)==sorted(t)
        #solution 2, same like solution 3
        return Counter(s) == Counter(t)
        #solution 3
        if(len(s)!=len(t)):
            return False
        countS,countT={},{} # use defaultdict(list) instead to avoid key not found error, it return a [] by defualt. defaultdict(str) returns "", defaultdict("Not present") by default
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0) #countS[s[i]] is previously not present error key not found. So .get() would initialize the value instead.
            countT[t[i]]=1+countT.get(t[i],0)
        for c in countS:
            if(countS[c]!=countT.get(c,0)):#countT.get(c,0) to avoid key not found error again
                return False
        #instead of line 14 to 16, you can return countS==countT
        return True
