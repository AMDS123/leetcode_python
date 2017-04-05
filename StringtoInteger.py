# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases.
# If you want a challenge, please do not see below and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
#
# Update (2015-02-10):
# The signature of the C++ function had been updated.
# If you still see your function signature accepts a const char * argument,
# please click the reload button  to reset your code definition.
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        sign = 1
        base = 0
        l = len(str)
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        a_0 = ord('0')
        a_9 = ord('9')
        while i < l and str[i] == ' ':
            i += 1
        if i < l and str[i] == '-':
            sign = -1
            i += 1
        elif i< l and str[i] == '+':
            i += 1
        while i < l and ord(str[i]) >= a_0 and ord(str[i]) <= a_9:
            if base > INT_MAX / 10 or (base == INT_MAX / 10 and ord(str[i]) - a_0 > 7):
                return sign == 1 and INT_MAX or INT_MIN
            base = 10 * base + (ord(str[i]) - a_0)
            i += 1

        return base * sign
