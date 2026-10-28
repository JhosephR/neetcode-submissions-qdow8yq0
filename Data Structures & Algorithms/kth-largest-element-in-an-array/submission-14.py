class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot = nums[right]
            i = left

            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i

        l, r = 0, len(nums) - 1
        k = len(nums) - k
        while l <= r:
            p = partition(l, r)
            if p < k:
                l = p + 1
            elif p > k:
                r = p - 1
            else:
                break
        return nums[p]