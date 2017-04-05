# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        l = (m + n + 1) // 2
        r = (m + n + 2) // 2
        return (self.getkth(nums1, 0, nums2, 0, l) + self.getkth(nums1, 0, nums2, 0, r)) / 2.0


    def getkth(self, A, aStart, B, bStart, k):
        if aStart > len(A) - 1:
            return B[bStart + k - 1]
        if bStart > len(B) - 1:
            return A[aStart + k - 1]
        if k == 1:
            return min(A[aStart], B[bStart])

        aMid = 9223372036854775807
        bMid = 9223372036854775807

        if aStart + k/2 - 1 < len(A):
            aMid = A[aStart + k//2 - 1]
        if bStart + k/2 - 1 < len(B):
            bMid = B[bStart + k//2 - 1]

        if aMid < bMid:
            return self.getkth(A, aStart + k//2, B, bStart, k-k//2)
        else:
            return self.getkth(A, aStart, B, bStart+k//2, k-k//2)