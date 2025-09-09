# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num = nums1[:m] + nums2[:n]
        for i in range(len(num)):
            if i < len(num)-1:
                for j in range(i+1, len(num)):
                    if num[i] > num [j]:
                        num[i], num[j] = num[j], num[i]
        for i in range(len(num)):
            nums1[i] = num[i]
        return nums1

        

print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))  # Output: [1,2,2,3,5,6]
print(Solution().merge([1],1,[],0))  # Output: [1]
print(Solution().merge([0],0,[1],1))  # Output: [1]