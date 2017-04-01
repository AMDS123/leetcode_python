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