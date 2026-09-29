# Using sorted array
# TC: O(nlogn)
# SC: O(n) or O(1) depending on the sorting algorithm used
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(1,len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1]:
                return True
        return False

        