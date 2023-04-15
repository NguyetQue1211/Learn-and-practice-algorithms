"""
Prompt: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

Example 1: 
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

Example 2: 
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints: 
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

Credit: 
This prompt is belong to leetcode study plan named: leetcode 75
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(nums[i])
            else:
                result.append(result[i-1]+nums[i])
        return result