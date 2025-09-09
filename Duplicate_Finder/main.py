#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. without using sets or dictionaries.
class Solution(object):
    def containsDuplicate(self,nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
    
print(Solution().containsDuplicate([1,2,3,1]))  # Output: True
print(Solution().containsDuplicate([1,2,3,4]))  # Output: False
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # Output: True