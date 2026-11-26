class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap = defaultdict(int)
        # freq, res  = [], []
        # for n in nums:
        #     hashmap[n] += 1
        # for key, value in hashmap.items():
        #     freq.append([value,key])
        # freq.sort()
        # for i in range(len(freq)-1,-1,-1):
        #     res.append(freq[i][1])
        #     if len(res) == k:
        #         break
        # return res   

        hashmap = defaultdict(int)
        freq, res  = [], []
        heap = []
        for n in nums:
            hashmap[n] += 1
        for num, cnt in hashmap.items():
            heapq.heappush(heap,(cnt,num))
            if len(heap) > k:
                heapq.heappop(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        


