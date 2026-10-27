import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(l, r):
            if l >= r:   # skip if list length is 1 or 0
                return

            # Randomized pivot prevents O(n^2) on already/nearly sorted arrays
            rand = random.randint(l, r)  
            nums[rand], nums[r] = nums[r], nums[rand]

            # 3-way partition (Dutch National Flag Algorithm) - For duplicate numbers
            low = l
            mid = l # scans the array l to r
            high = r

            pivot = nums[r]

            while mid <= high:                               
                if nums[mid] < pivot:   # move lower numbers to the l of pivot
                    nums[mid], nums[low] = nums[low], nums[mid]
                    low += 1
                    mid += 1
                elif nums[mid] > pivot: # move higher numbers to the r of pivot
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1
                else:                   # equal elements stay in the middle section
                    mid += 1

            # pivot boundaries == low ... high (already sorted)
            quickSort(l, low - 1)    # sort numbers < pivot
            quickSort(high + 1, r)  # sort numbers > pivot

        quickSort(0, len(nums) - 1)
        return nums