class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() #values
        ans = []
        l = 0

        for r in range(len(nums)):
            while q and nums[r] > q[-1]: # monotonic decreasing 4 3 2
                q.pop()
            q.append(nums[r])

            if (r - l + 1) == k:
                ans.append(q[0])
                if nums[l] == q[0]: # compare both left values
                    q.popleft()     # remove it from window
                l += 1
        return ans