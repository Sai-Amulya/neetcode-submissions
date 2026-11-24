class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # hashmap = defaultdict(list)
        # for s in strs:
        #     sortedS = "".join(sorted(s))
        #     # sortedS = tuple(sorted(s)) 
        #     hashmap[sortedS].append(s)
        # return list(hashmap.values())

        hashmap = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            hashmap[tuple(count)].append(s)
        return list(hashmap.values())

        