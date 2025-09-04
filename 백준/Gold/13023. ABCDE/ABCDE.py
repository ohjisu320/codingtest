import sys
input = sys.stdin.readline

def f(a, cnt) : # a: 친구1 인덱스, cnt: 연결된 인원 수
    if cnt == 4 : return True # 4명이 연결되면 종료
    for b in adj[a] : # a 친구들 탐색
        if not visited[b] : # a 친구들 중에 확인 안한 애가 있으면
            visited[b] = True # 방문 표시
            if f(b, cnt + 1) : return True # a 친구 b 확인하기
            visited[b] = False # 통과 못하면 방문표시 초기화
    return False # 다 돌았는데도 못찾으면 False 반환

N, M = map(int, input().split())

adj = [[] for _ in range(N)] # 인접 리스트 생성

for i in range(M) : # 간선 수 만큼
    a, b = map(int, input().split()) 
    adj[a].append(b) # 양방향으로 저장
    adj[b].append(a)

visited = [0] * N # N개 만큼 방문 표시 위함
flag = 0 # 잘 찾았는지 확인
for i in range(N) : # 인접리스트 순회 및 방문 표시를 위한 i
    visited[i] = True # 방문 표시
    if f(i, 0) == True : # cnt == 4인걸 찾으면
        print(1)         # print(1) 찍고 종료
        flag = 1
        break
    visited[i] = False   # 아니면 다음거 탐색을 위해 visited 초기화
if not flag : print(0) # 잘 못찾았으면 print(0)