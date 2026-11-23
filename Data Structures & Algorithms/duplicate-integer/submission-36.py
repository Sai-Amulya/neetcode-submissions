class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        return len(nums) != len(set(nums))



        # brute force: O(n^2), O(1)
        # sorting : O(nlogn + n), O(1) or O(n)
        # hashset: O(n + n + n), O(n)
        # hashset length: O(n + n), O(n)








        