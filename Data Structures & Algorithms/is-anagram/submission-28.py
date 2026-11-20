class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sortedS = sorted(s)
        # sortedT = sorted(t)
        # return sortedS == sortedT

        if len(s) != len(t):
            return False
        hashmap_s = defaultdict(int)
        hashmap_t = defaultdict(int)
        for i in range(len(s)):
            hashmap_s[s[i]] += 1
            hashmap_t[t[i]] += 1
        return hashmap_s == hashmap_t

        