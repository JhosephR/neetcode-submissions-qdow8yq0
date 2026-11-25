class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stacks = [[]]

    def push(self, val: int) -> None:
        self.freq[val] = 1 + self.freq.get(val, 0)
        if self.freq[val] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.freq[val]].append(val)

    def pop(self) -> int:
        ans = self.stacks[-1].pop()
        self.freq[ans] -= 1
        if not self.stacks[-1]:
            self.stacks.pop()
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()