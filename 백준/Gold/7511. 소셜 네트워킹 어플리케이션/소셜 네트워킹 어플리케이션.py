import sys
sys.setrecursionlimit(1000)
input = lambda : sys.stdin.readline().rstrip()

def find_set(x) :
    # 만약 내가 대표자면 나 출력
    if parents[x] == x :
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union_set(x, y) :
    px = find_set(x)
    py = find_set(y)

    # 둘이 친구인지 확인
    if px == py :
        return
    elif px < py :
        parents[py] = px
    else :
        parents[px] = py


T = int(input())
for t in range(1, T+1) :
    n = int(input()) # 유저의 수
    k = int(input()) # 친구 관계의 수

    # Todo: 나를 대표자로 설정하는 parents 만들기
    parents = [i for i in range(n)]

    for _ in range(k) :
        a, b = map(int, input().split())

        # 친구가 아니면 친구로 연결
        union_set(a, b)

    print(f"Scenario {t}:")
    m = int(input())  # 구할 쌍의 개수
    for _ in range(m) :
        c, d = map(int, input().split())
        # 친구인지 확인, 친구면 1, 아니면 0 출력
        if find_set(c) == find_set(d) :
            print(1)
        else :
            print(0)

    # 각 테스트 케이스 사이에 빈 줄 출력
    if t < T:
        print()