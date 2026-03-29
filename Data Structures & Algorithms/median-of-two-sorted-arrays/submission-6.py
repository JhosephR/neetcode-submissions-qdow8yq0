class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            m1 = l + ((r - l) // 2)
            m2 = half - m1 - 2

            AL = A[m1] if m1 >= 0 else float("-inf")
            AR = A[m1 + 1] if (m1 + 1) < len(A) else float("inf")

            BL = B[m2] if m2 >= 0 else float("-inf")
            BR = B[m2 + 1] if (m2 + 1) < len(B) else float("inf")

            if AL <= BR and BL <= AR:
                if total % 2:   # odd
                    return min(AR, BR)
                else:           # even
                    return (max(AL, BL) + min(AR, BR)) / 2
            elif AL > BR:
                r = m1 - 1
            else:
                l = m1 + 1