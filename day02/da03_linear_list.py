# 선형리스트 일반 구현
# 실제 파이썬이 이렇게 동작하는 게 아님!
# 배열(선형리스트)이 어떻게 동작하는지 로직을 파악할 것!
## 전역변수 선언 부분
katok = [] # 빈 배열
select = -1 # -1:통과, 1:추가, 2:삽입, 3:삭제, 4:종료

def add_data(friend):
    katok.append(None)
    lenKatok = len(katok)
    katok[lenKatok - 1] = friend

# 중간 데이터 삽입
def insert_data(pos, friend):
    # 잘못된 인덱스를 넣었을때 예외처리 필요
    if pos < 0 or pos > len(katok):
        print('실행할 범위를 벗어났습니다.')
        return

    katok.append(None)
    lenkatok = len(katok)

    for i in range(lenkatok - 1, pos, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[pos] = friend

def delete_data(pos):
    if pos < 0 or pos > len(katok):
        print('삭제 범위를 벗어났습니다.')
        return
    
    lenKatok = len(katok)
    katok[3] = None # 지정된위치 값을 삭제

    for i in range(3+1, lenKatok):
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[lenKatok-1]) # 배열 맨마지막 삭제

## 메인코드 영역
if __name__ == '__main__':
    while True:
        select = int(input('선택(1:추가, 2:삽입, 3:삭제, 4:종료) > '))

        if select == 1:
            data = input('추가 데이터-->')
            add_data(data)
            print(katok)
        elif select == 2:
            pos, data = input('삽입위치, 데이터 입력 -->').split()
            pos = int(pos)
            insert_data(pos, data)
            print(katok)
        elif select == 3:
            pos = int(input('삭제위치-->'))
            delete_data(pos)
            print(katok)
        elif select == 4:
            break
        else:
            print('1 ~ 4 중 입력할 것')
            continue

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('다현')
add_data('지효')
print(katok)

insert_data(2, '솔라')
print(katok)
insert_data(6, '문별')

print(katok)


