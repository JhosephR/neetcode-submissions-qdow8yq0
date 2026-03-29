class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            m1 = l + ((r - l) // 2)
            m2 = ((len(A) + len(B)) // 2) - m1 - 2
            
            AL = A[m1] if m1 >= 0 else float("-infinity")
            AR = A[m1 + 1] if (m1 + 1) < len(A) else float("infinity")
            BL = B[m2] if m2 >= 0 else float("-infinity")
            BR = B[m2 + 1] if (m2 + 1) < len(B) else float("infinity")

            if AL <= BR and BL <= AR:
                if (len(A) + len(B)) % 2: # odd
                    return min(AR, BR)
                return (max(AL, BL) + min(AR, BR)) / 2
            elif AL > BR:
                r = m1 - 1
            else:
                l = m1 + 1