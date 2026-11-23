class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        













# 1. sort and check equality - O(mlogm + nlogn), O(m+n)
# 2. hashmap - record frequency and check equality
# 3. hashtable - array of size 26 and all must be 0 if anagrams
    

        