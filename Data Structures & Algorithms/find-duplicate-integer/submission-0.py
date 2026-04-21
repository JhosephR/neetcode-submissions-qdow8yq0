class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return n
            hashSet.add(n)
