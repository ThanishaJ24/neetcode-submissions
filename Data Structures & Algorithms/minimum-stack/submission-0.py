class MinStack:

    def __init__(self):
        self.stack=[]
        self.Top=-1
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.Top+=1
        

    def pop(self) -> None:
        self.stack.pop()
        self.Top-=1
        

    def top(self) -> int:
        return self.stack[self.Top]

        

    def getMin(self) -> int:
        return min(self.stack)
        
