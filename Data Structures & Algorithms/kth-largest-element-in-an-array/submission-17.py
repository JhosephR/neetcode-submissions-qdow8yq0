import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        def quickSelect(l, r):
            if l >= r:
                return nums[l]
            
            # Simplidied Median-of-Three Pivot Selection
            mid = l + (r - l) // 2

            if nums[mid] < nums[l]:
                nums[mid], nums[l] = nums[l], nums[mid]
            if nums[r] < nums[l]:
                nums[r], nums[l] = nums[l], nums[r]
            if nums[r] < nums[mid]:
                nums[r], nums[mid] = nums[mid], nums[r]
            
            nums[mid], nums[r] = nums[r], nums[mid]

            low = l
            mid = l
            high = r

            pivot = nums[r]

            while mid <= high:
                if nums[mid] < pivot:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low += 1
                    mid += 1
                elif nums[mid] > pivot:
                    nums[high], nums[mid] = nums[mid], nums[high]
                    high -= 1
                else:
                    mid += 1

            if target > low:
                return quickSelect(low + 1, r)
            elif target < high:
                return quickSelect(l, high - 1)
            else:
                return nums[target]
        return quickSelect(0, len(nums) - 1)