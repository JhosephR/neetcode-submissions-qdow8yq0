class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while r < len(numbers):
            sm = numbers[l] + numbers[r]
            if sm == target:
                return [l+1,r+1]
            if l < r and sm < target:
                l += 1
            elif r > l and sm > target:
                r -= 1
        return [l+1,r+1]