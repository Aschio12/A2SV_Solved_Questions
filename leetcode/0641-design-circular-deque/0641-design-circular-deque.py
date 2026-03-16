class MyCircularDeque:

    def __init__(self, k: int):
        self.k=k
        self.front=0
        self.size=0
        self.queue=[0]*k

    def insertFront(self, value: int) -> bool:
        if self.isFull():return False
        self.front=(self.front-1+self.k)%self.k
        self.queue[self.front]=value
        self.size+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():return False
        last=(self.front+self.size)%self.k
        self.queue[last]=value
        self.size+=1    
        return True    

    def deleteFront(self) -> bool:
        if self.isEmpty():return False
        self.front=(self.front+1)%self.k
        self.size-=1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():return False
        self.size-=1
        return True
        
    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]  

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.queue[(self.front+self.size-1)%self.k]   

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()