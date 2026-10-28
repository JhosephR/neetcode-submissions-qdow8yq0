import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(l, r):
            if l >= r:
                return nums[l]
            
            random_i = random.randint(l, r)
            nums[random_i], nums[r] = nums[r], nums[random_i]
            
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

            if k > low:
                return quickSelect(low + 1, r)
            elif k < high:
                return quickSelect(l, high - 1)
            else:
                return nums[k]
        return quickSelect(0, len(nums) - 1)