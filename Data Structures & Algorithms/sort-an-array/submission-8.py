import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(l, r):
            if l >= r:
                return
            
            random_i = random.randint(l, r)
            nums[random_i], nums[r] = nums[r], nums[random_i]

            low = curr = l
            high = r
            pivot = nums[r]

            while curr <= high:
                if nums[curr] < pivot:
                    nums[low], nums[curr] = nums[curr], nums[low]
                    low += 1
                    curr += 1
                elif nums[curr] > pivot:
                    nums[curr], nums[high] = nums[high], nums[curr]
                    high -= 1
                else:
                    curr += 1
            quickSort(l, low - 1)
            quickSort(high + 1, r)
        quickSort(0, len(nums) - 1)
        return nums