# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# click to show spoilers.
#
# Note:
# The input is assumed to be a 32-bit signed integer.
# Your function should return 0 when the reversed integer overflows.
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        flag = x < 0 and -1 or 1
        x *= flag
        while x != 0:
            res = res * 10 + x % 10
            x /= 10
        if res > 2147483647:
            return 0
        return res * flag