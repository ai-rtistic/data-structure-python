# 함수 선언
def isStackFull() :    # 스택이 꽉 찼는지 확인
	global SIZE, stack, top
	if (top >= SIZE-1) :
		return True
	else :
		return False

def isStackEmpty() :    # 스택이 비었는지 확인
	global SIZE, stack, top
	if (top == -1) :
		return True
	else :
		return False

def push(data) :
	global SIZE, stack, top
	if (isStackFull()) :
		print("Stack full")
		return
	top += 1
	stack[top] = data

def pop() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		print("Stack empty")
		return None
	data = stack[top]
	stack[top] = None
	top -= 1
	return data

def peek() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		print("Stack empty")
		return None
	return stack[top]

# 전역 변수
SIZE = int(input("Stack size : "))
stack = [ None for _ in range(SIZE) ]
top = -1

# 메인 코드
if __name__ == "__main__" :
	select = input("Insert(I)/Extract(E)/Verify(V)/Exit(X) : ")

	while (select != 'X' and select != 'x') :
		if select=='I' or select =='i' :
			data = input("Insert data :  ")
			push(data)
			print("Stack : ", stack)
		elif select=='E' or select =='e' :
			data = pop()
			print("Extracted data :  ", data)
			print("Stack : ", stack)
		elif select=='V' or select =='v' :
			data = peek()
			print("Verified data : ", data)
			print("Stack : ", stack)
		else :
			print("Wrong input")

		select = input("Insert(I)/Extract(E)/Verify(V)/Exit(X) : ")

	print("End program")