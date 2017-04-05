# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
# Example:
#
# Input: "cbbd"
#
# Output: "bb"
class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        curLength = 0
        for i in xrange(len(s)):
            if self.isPalindrome(s, i - curLength - 1, i):
                res = s[i - curLength - 1 : i + 1]
                curLength += 2
            elif self.isPalindrome(s, i - curLength, i):
                res = s[i - curLength : i + 1]
                curLength += 1
        return res

    def isPalindrome(self, s, begin, end):
        if begin < 0:
            return False
        while begin < end:
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        return True

