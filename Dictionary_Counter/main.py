# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # count_dict = {}
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        max_count = 0
        majority_element = None
        for num, count in count_dict.items():
            if count > max_count:
                max_count = count
                majority_element = num
        return majority_element
    

# print(Solution.majorityElement(3, [3,2,3]))
print(Solution().majorityElement([3,2,3]))  # Output: 3