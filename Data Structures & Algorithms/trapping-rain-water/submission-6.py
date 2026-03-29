class Solution:
    def trap(self, height: List[int]) -> int:
        d, amount, l, t = {}, 0, 0, -1
        for i in range(len(height)):
            d[i] = height[i]
        
        while height[l] == 0:
            l += 1
            if l >= len(height):
                return amount
        r = l + 1

        while r < len(height):
            while height[r] == 0:
                r += 1
                if r >= len(height):
                    return amount
            h = min(height[l], height[r]) #1
            c = 0
            for i in range(l+1,r):
                water = h - d[i]
                if water < 0:
                    continue
                c += 1
                amount += water
                d[i] = h
            if t == -1 and height[l] > height[r]:
                t = l
            if t == -1 and height[l] < height[r]:
                t = r
            if t != -1:
                h = min(height[t], height[r]) #2
                c = 0
                for i in range(t+1,r):
                    water = h - d[i]
                    if water < 0:
                        continue
                    c += 1
                    amount += water
                    d[i] = h

            if height[l] > height[r]:
                if height[l] > height[t]:
                    t = l
            elif height[l] < height[r]:
                if height[r] > height[t]:
                    t = r
            elif height[t] == height[r]:
                t = r

            if c > 0:
                l = r
            r += 1
        return amount