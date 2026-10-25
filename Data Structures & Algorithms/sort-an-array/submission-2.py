import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(left, right):
            if left >= right:
                return

            random_index = random.randint(left, right)
            nums[random_index], nums[right] = nums[right], nums[random_index]

            low = left
            mid = left
            high = right

            pivot = nums[right]

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
            quickSort(left, low - 1)
            quickSort(high + 1, right)

        quickSort(0, len(nums) - 1)
        return nums