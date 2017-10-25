# URL: https://leetcode.com/problems/two-sum/description/
# 
# Description:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        end = len(nums)
        d = {}

        for i, n in enumerate(nums):
            remainder = target - n

            if remainder in d:
                return [d[remainder], i]
            else:
                d[n] = i



nums = [1,2,3,4,5,6,7,8,9,10]
target = 15

o = Solution()
result = o.twoSum(nums, target)
print(result)
