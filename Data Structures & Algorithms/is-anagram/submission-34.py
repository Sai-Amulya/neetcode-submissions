class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT

        

# 1. sort and check equality - O(mlogm + nlogn), O(m+n)
# 2. hashmap - record frequency and check equality - O(n+m+n), O(1) as 26
# 3. hashtable - array of size 26 and all must be 0 if anagrams
    

        