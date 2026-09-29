# More optimal - using hashset length
# TC: O(n)
# SC: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set(nums)
        if len(hashset) < len(nums):
            return True
        else:
            return False

        