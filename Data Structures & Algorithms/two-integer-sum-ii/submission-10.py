class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sm = numbers[l] + numbers[r]
            if sm < target:
                l += 1
                while l < r and numbers[l] == numbers[l-1]:
                    l += 1
            elif sm > target:
                r -= 1
                while r > l and numbers[r] == numbers[r+1]:
                    r -= 1
            else:
                return [l+1, r+1]
        return []