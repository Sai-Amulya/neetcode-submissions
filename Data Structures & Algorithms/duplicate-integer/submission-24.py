# Sort and compare adjacent - O(nlogn) O(1) or O(n)
# range starts from 1 as i -1 should be able to check 0 and not go out of bounds
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)): # Remember: check notes
            if nums[i] == nums[i-1]:
                return True
        return False
        