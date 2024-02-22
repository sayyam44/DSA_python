class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[] #in order to min vals till now

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
        #appending the min value among the current val and the topmost value in minstack if exists into minstack
        
    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1] #min value is always gonna be on the top of minstack
        


