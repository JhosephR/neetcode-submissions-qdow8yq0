import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(l, r):
            if l >= r:
                return
            
            random_i = random.randint(l, r)
            nums[random_i], nums[r] = nums[r], nums[random_i]

            low = l
            mid = l
            high = r

            pivot = nums[r]

            while mid <= high:
                if nums[mid] < pivot:
                    nums[mid], nums[low] = nums[low], nums[mid]
                    low += 1
                    mid += 1
                elif nums[mid] > pivot:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1
                else:
                    mid += 1
            
            quickSort(l, low - 1)
            quickSort(high + 1, r)
        quickSort(0, len(nums) - 1)
        return nums