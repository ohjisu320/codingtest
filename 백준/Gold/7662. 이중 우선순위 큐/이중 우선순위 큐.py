from heapq import heappush, heappop

T = int(input()) # 테스트케이스
for _ in range(T) :
    k = int(input()) # 연산 수행하는 횟수
    min_hq = []
    max_hq = []
    visited = [0] * k # 힙에 들어간 숫자 체크용

    for i in range(k) :
        command, n = input().split()
        n = int(n)

        if command == 'I' :
            heappush(min_hq, (n, i))
            heappush(max_hq, (-n, i))
            visited[i] = 1

        else :
            if n == 1 :
                while max_hq and not visited[max_hq[0][1]]:
                    heappop(max_hq)
                if max_hq :
                    visited[max_hq[0][1]] = 0
                    heappop(max_hq)
            elif n == -1:
                while min_hq and not visited[min_hq[0][1]] :
                    heappop(min_hq)
                if min_hq :
                    visited[min_hq[0][1]] = 0
                    heappop(min_hq)


    while max_hq and not visited[max_hq[0][1]]:
        heappop(max_hq)
    while min_hq and not visited[min_hq[0][1]]:
        heappop(min_hq)

    if min_hq and max_hq :
        print(-heappop(max_hq)[0], heappop(min_hq)[0])
    else :
        print('EMPTY')