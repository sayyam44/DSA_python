front=rear=0
def createqueue():
    queue=[]
    return queue

def enqueue(queue,val):
    if rear==len(queue):
        print('queue is full')
    elif rear<len(queue):
        queue.append(val)
        rear+=1

def dequeue(queue):
    if front==rear:
        print('queue is empty')
    else:
        queue.pop(front)
        rear-=1 #all the remaining elements have to shifted to the left by one position in order for the 
        # dequeue operation to delete the second element from the left on another dequeue operation.

def queuedisplay(queue):
    if front==rear:
        print('queue is empty')
    for i in range queue:
        print(i,end=" ")

def queuefront(queue):
    if front==rear:
        print('queue is empty')
    else:
        return (queue[front])

queue = createqueue()
enqueue(queue,str(10))
enqueue(queue, str(20))
enqueue(queue, str(30))



