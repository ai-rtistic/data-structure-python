class CircleQueue:
	def __init__(self, size):
		self.size = size
		self.queue = [i for i in range(self.size)]
		self.front = 0
		self.rear = 0
    
	def is_empty(self):    # 큐가 비었는지 확인
		if self.rear == self.front:
			return True
		return False

	def is_full(self):    # 큐가 꽉 찼는지 확인
		if (self.rear+1)%self.size == self.front:
			return True
		return False

	def enqueue(self, x):
		if self.is_full():
			print("ERROR: FULL")
			return
		self.rear = (self.rear+1)%(self.size)
		self.queue[self.rear] = x
	
	def dequeue(self):
		if self.is_empty():
			print("ERROR: EMPTY")
			return
		self.front = (self.front +1) % self.size
		return self.queue[self.front]

	def peek(self):    
		i = self.front
		if self.is_empty():
			print("EMPTY QUEUE")
			return
		while True:
			i = (i+1)%self.size
			print(self.queue[i], ' ')
			if i == self.rear or i != self.front:
				break
	
	def queue_print(self):   # 현재 큐 전체 출력
		print(self.queue)
