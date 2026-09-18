class MinStack:

    def __init__(self):
        self.stack = []
        self.m_stack = []
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.m_stack.append(val)
        else:
            if val < self.m_stack[-1]:
                self.m_stack.append(val)
                self.stack.append(val)
            else:
                self.m_stack.append(self.m_stack[-1])
                self.stack.append(val)

    def pop(self) -> None:
        self.m_stack.pop(-1)
        return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m_stack[-1]
        
