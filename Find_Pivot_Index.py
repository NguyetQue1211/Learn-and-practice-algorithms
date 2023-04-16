"""
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Example 1: 
Input: nums = [1,7,3,6,5,6]
Output: 3

Example 2: 
Input: nums = [1,2,3]
Output: -1

Constraints: 
1 <= nums.length <= 10^84
-1000 <= nums[i] <= 1000

Credit: 
This prompt is belong to leetcode study plan named: leetcode 75
"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i == 0: 
                right_nums = nums[1:]
                if sum(right_nums) == 0:
                    return 0
            else: 
                left_nums = nums[:i]
                right_nums = nums[i+1:]
                if sum(left_nums) == sum(right_nums): 
                    return i
        return -1