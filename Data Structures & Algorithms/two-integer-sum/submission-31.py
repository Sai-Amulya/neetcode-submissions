class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []

        # indices = []
        # for i,n in enumerate(nums):
        #     indices.append([n,i])
        # indices.sort()
        # i,j = 0,len(indices)-1
        # while i<j:
        #     add = indices[i][0] + indices[j][0]
        #     if add == target:
        #         return [min(indices[i][1],indices[j][1]),
        #                 max(indices[i][1],indices[j][1])]
        #     elif add < target:
        #         i+=1
        #     else:
        #         j-=1
        # return []

        # hashmap = {}
        # for i,n in enumerate(nums):
        #     hashmap[n] = i
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in hashmap and hashmap[diff]!=i:
        #         return [i, hashmap[diff]]
        # return []

        indices = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indices:
                return [indices[diff], i]
            indices[nums[i]] = i

        