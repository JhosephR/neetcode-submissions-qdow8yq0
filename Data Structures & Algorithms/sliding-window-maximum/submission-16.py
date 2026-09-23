class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, ans, q = 0, [], deque() # Monotonic decreasing 5 4 3...
        for r in range(len(nums)):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])

            if (r - l + 1) == k:
                ans.append(q[0])
                if nums[l] == q[0]:
                    q.popleft()
                l += 1
        return ans