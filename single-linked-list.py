# 단순 연결 리스트

# 전역 변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ["A", "B", "C", "D", "E"]


# 클래스 및 함수 구현
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

# 데이터 출력
def printNodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()


# 데이터 검색
def findNode(find_data) :
	global memory, head, current, pre

	current = head
	if current.data == find_data :
		return current
	while current.link != None :
		current = current.link
		if current.data == find_data :
			return current
	return Node()	# 빈 노드 반환

# 데이터 index 출력
def getdataIndex(data):
    current = head
    idx = 0
    while current != None:
        if current.data == data:
            return idx
        current = current.link
        idx += 1
    return None



# 데이터 삽입
def insertNode(find_data, insert_data) :
	global memory, head, current, pre

	if head.data == find_data :      # 첫 번째 부분 삽입
		node = Node()
		node.data = insert_data
		node.link = head
		head = node
		return

	current = head
	while current.link != None :    # 중간 부분 삽입
		pre = current
		current = current.link
		if current.data == find_data :
			node = Node()
			node.data = insert_data
			node.link = current
			pre.link = node
			return

	node = Node()                   # 마지막 부분 삽입
	node.data = insert_data
	current.link = node

# 데이터 삭제
def deleteNode(delete_data) :
	global memory, head, current, pre

	if head.data == delete_data :         # 첫 번째 노드 삭제
		current = head
		head = head.link
		del(current)
		return

	current = head                          # 첫 번째  외 노드 삭제
	while current.link != None :
		pre = current
		current = current.link
		if current.data == delete_data :
			pre.link = current.link
			del(current)
			return


# 메인 코드
if __name__ == "__main__" :

	node = Node()			# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :		# 두 번째 노드부터
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		memory.append(node)

	printNodes(head)    # A B C D E
	print(getdataIndex('C'))    # 2
