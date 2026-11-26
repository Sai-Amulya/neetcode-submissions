class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        freq, res  = [], []
        for n in nums:
            hashmap[n] += 1
        for key, value in hashmap.items():
            freq.append([value,key])
        freq.sort()
        for i in range(len(freq)-1,-1,-1):
            res.append(freq[i][1])
            if len(res) == k:
                break
        return res    

