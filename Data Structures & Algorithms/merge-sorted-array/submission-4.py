class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy = nums1[:m]
        l = r = 0

        for i in range(m + n):
            if r < n:
                if l < m and copy[l] < nums2[r]:
                    nums1[i] = copy[l]
                    l += 1
                else:
                    nums1[i] = nums2[r]
                    r += 1
            else:
                nums1[i] = copy[l]
                l += 1