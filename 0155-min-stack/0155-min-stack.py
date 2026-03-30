class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        latest_min = self.min_stack[-1][0] if self.min_stack else 2**63-1
        if latest_min == val:
            self.min_stack[-1][1] += 1
        elif latest_min > val:
            self.min_stack.append([val, 1])

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1][0]:
            if self.min_stack[-1][1] > 1:
                self.min_stack[-1][1] -= 1
            else:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()