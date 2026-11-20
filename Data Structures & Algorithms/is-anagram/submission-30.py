class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
            # return False
        # return sorted(s) == sorted(t)

        # if len(s) != len(t):
        #     return False
        # hashmap_s = defaultdict(int)
        # hashmap_t = defaultdict(int)
        # for i in range(len(s)):
        #     hashmap_s[s[i]] += 1
        #     hashmap_t[t[i]] += 1
        #        or without defaultdict hashmap_s[s[i]] = 1 + hashmap_s.get(s[i],0)
        #        or without defaultdict hashmap_t[t[i]] = 1 + hashmap_t.get(t[i],0)
        # return hashmap_s == hashmap_t

        if len(s) != len(t):
            return False
        table = [0] * 26
        for i in range(len(s)):
            table[ord(s[i])-ord('a')] += 1
            table[ord(t[i])-ord('a')] -= 1
        for i in range(len(table)):
            if table[i] != 0:
                return False
        return True
    

        