class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, pos, ans = [1], [1], []
        i, j, k, l = 0, -1, 0, -2

        while i < len(nums):
            pre.append(pre[i] * nums[i])
            pos.append(pos[i] * nums[j])
            i += 1
            j -= 1

        while k < len(nums):
            ans.append(pre[k] * pos[l])
            k += 1
            l -= 1

        return ans