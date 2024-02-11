
#TC for push=0(1)
#TC for pop,peek=o(1) amonitised

class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if len(self.s1) == 0 and len(self.s2) == 0:
            return
        elif len(self.s1)>0 and len(self.s2)==0:
            while len(self.s1):
                temp=self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
        else:
            return self.s2.pop()

    def peek(self) -> int:
        if len(self.s1) == 0 and len(self.s2) == 0:
            return
        elif len(self.s1)>0 and len(self.s2)==0:
            while len(self.s1):
                temp=self.s1.pop()
                self.s2.append(temp)
            return self.s2[-1]
        else:
            return self.s2[-1]
    def empty(self) -> bool:
        return (len(self.s1)==0 and len(self.s2)==0)
        
