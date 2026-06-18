class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, l, ans = deque(), 0, []

        for r in range(len(nums)):
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])

            if (r - l + 1) == k:
                ans.append(q[0])
                if nums[l] == q[0]:
                    q.popleft()
                l += 1
        return ans