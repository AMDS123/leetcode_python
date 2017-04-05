# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in xrange(len(nums)):
            map[nums[i]] = i
        for i in xrange(len(nums)):
            num = nums[i]
            num1 = target - num
            if map.has_key(num1):
                j = map[num1]
                if i != j:
                    return [i,j]

result = Solution().twoSum([2,7,11,15], 9)
print(result)