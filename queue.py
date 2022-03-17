# 선형리스트를 이용해 큐를 구현
# 함수 선언
def isQueueFull() :    # 큐가 꽉 찼는지 확인
	global SIZE, queue, front, rear
	if (rear == SIZE-1) :
		return True
	else :
		return False

def isQueueEmpty() :    # 큐가 비었는지 확인
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False

def enQueue(data) :    # 데이터 삽입
	global SIZE, queue, front, rear
	if (isQueueFull()) :
		print("Queue Full")
		return
	rear += 1
	queue[rear] = data

def deQueue() :    # 데이터 삭제
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("Queue Empty")
		return None
	data = queue[front+1]
	for i in range(0, SIZE-1):
		queue[i] = queue[i+1]
	queue[-1] = None
	rear -= 1
	return data

def peek() :    # 가장 먼저들어온(front) 데이터 확인
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("Queue Empty")
		return None
	return queue[front+1]

# 전역 변수 선언
SIZE = int(input("Queue Size : "))
queue = [ None for _ in range(SIZE) ]
front = rear = -1

# 메인 코드
if __name__ == "__main__" :
	select = input("Insert(I)/Extract(E)/Verify(V)/Exit(X) : ")

	while (select != 'X' and select != 'x') :
		if select=='I' or select =='i' :
			data = input("Insert data : ")
			enQueue(data)
			print("Queue : ", queue)
		elif select=='E' or select =='e' :
			data = deQueue()
			print("Extracted data : ", data)
			print("Queue : ", queue)
		elif select=='V' or select =='v' :
			data = peek()
			print("Verified data : ", data)
			print("Queue : ", queue)
		else :
			print("Wrong input")

		select = input("Insert(I)/Extract(E)/Verify(V)/Exit(X) : ")

	print("End program")



#####


# 연결리스트(linked list)를 이용해 큐를 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedListQueue():
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, data):
        new_node = Node(data)
        
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.link = new_node
            self.rear = self.rear.link
        
    def dequeue(self):
        dequeue_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            dequeue_object = self.front.data
            self.front = self.front.link
            
        if self.front is None:
            self.rear = None
        return dequeue_object
    
    def peek(self):
        front_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            front_object = self.front.data            
        return front_object
    
    def isEmpty(self):
        is_empty = False
        if self.front is None:
            is_empty = True
        return is_empty