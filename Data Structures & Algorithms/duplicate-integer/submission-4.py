class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for n in nums:
            if n in myMap:
                myMap[n] += 1
                if myMap[n] > 1:
                    return True
            else:
                myMap[n] = 1
        return False
            