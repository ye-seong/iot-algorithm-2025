# 원형 큐 구현

def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear+1) % SIZE == front):
        return True
    else:
        return False
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear+1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    return queue[(front+1)%SIZE]

# 전역 변수 선언 부분
SIZE = int(input("큐 크기를 입력하세요 ==> "))
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ").upper()

    while True:
        if select == 'I':
            data = input("입력할 데이터 ==> ")
            enQueue(data)
            print(f"큐 상태 : {queue}")
            print(f"front : {front}, rear : {rear}")
        elif select == 'E':
            data = deQueue()
            print(f"추출된 데이터 ==> {data}")
            print(f"큐 상태 : {queue}")
            print(f"front : {front}, rear : {rear}")
        elif select == 'V':
            data = peek()
            print(f"확인된 데이터 ==> {data}")
            print(f"큐 상태 : {queue}")
            print(f"front : {front}, rear : {rear}")
        elif select == 'X':
            print("프로그램 종료!")
            break
        else:
            print("입력 오류")

