class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(l, r):
            i = l
            pivot = nums[r]

            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]

            while l <= r:
                if i < k:
                    return quickSelect(i + 1, r)
                elif i > k:
                    return quickSelect(l, i - 1)
                else:
                    return nums[i]
        return quickSelect(0, len(nums) - 1)