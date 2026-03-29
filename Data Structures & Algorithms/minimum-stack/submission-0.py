class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.prefix_mins:
            self.prefix_mins.append(min(self.prefix_mins[-1],val))
        else:
            self.prefix_mins.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.prefix_mins.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.prefix_mins:
            return self.prefix_mins[-1]
