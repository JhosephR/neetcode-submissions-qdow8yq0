import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(left, right):
            if left >= right:   # skip if list length is 1 or 0
                return

            # Randomized pivot to prevent O(n^2) on already or nearly sorted arrays
            random_i = random.randint(left, right)  
            nums[random_i], nums[right] = nums[right], nums[random_i]

            # 3-way partition (Dutch National Flag Algorithm) - For duplicate numbers
            low = left
            mid = left
            high = right

            pivot = nums[right]

            while mid <= high:                               
                if nums[mid] < pivot:   # move lower numbers to the left of pivot
                    nums[mid], nums[low] = nums[low], nums[mid]
                    low += 1
                    mid += 1
                elif nums[mid] > pivot: # move higher numbers to the right of pivot
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1
                else:                   # equal elements stay in the middle section
                    mid += 1

            # pivot == low ... high (already sorted)
            quickSort(left, low - 1)    # sort numbers < pivot
            quickSort(high + 1, right)  # sort numbers > pivot

        quickSort(0, len(nums) - 1)
        return nums