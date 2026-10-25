import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(l, r):
            if l >= r:
                return
            
            random_i = random.randint(l,r)
            nums[random_i], nums[r] = nums[r], nums[random_i]

            i = l
            j = r
            k = l
            pivot = nums[r]

            while k <= j:
                if nums[k] < pivot:
                    nums[i], nums[k] = nums[k], nums[i]
                    i += 1
                    k += 1
                elif nums[k] > pivot:
                    nums[j], nums[k] = nums[k], nums[j]
                    j -= 1
                else:
                    k += 1
            quickSort(l, i - 1)
            quickSort(j + 1, r)

        quickSort(0, len(nums) - 1)
        return nums