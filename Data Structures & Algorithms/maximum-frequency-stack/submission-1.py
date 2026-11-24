class FreqStack:

    def __init__(self):
        self.freq = {}
        self.maxF = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        self.freq[val] = 1 + self.freq.get(val, 0)
        if self.freq[val] > self.maxF:
            self.maxF = self.freq[val]
            self.stacks[self.freq[val]] = []
        self.stacks[self.freq[val]].append(val)

    def pop(self) -> int:
        ans = self.stacks[self.maxF].pop()
        self.freq[ans] -= 1
        if not self.stacks[self.maxF]:
            self.maxF -= 1
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()