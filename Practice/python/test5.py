import sys, heapq

INF = float('inf')
input = sys.stdin.readline
ProblemCount = 0 # 문제 번호를 카운트하기 위한 변수

# 무한 반복문, 종료 조건은 N이 0일 때
while True:
    N = int(input())

    # N이 0이면 종료
    if N == 0: break

    # 동굴의 각 칸에 있는 도둑루피 정보를 2차원 리스트로 저장
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 최소 비용 테이블 초기화 (모든 값을 INF로 설정)
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = graph[0][0]# 시작 지점의 최소 비용은 해당 칸의 값으로 초기화

    # 우선순위 큐 (힙) 초기화: (비용, y좌표, x좌표)
    heap = [[graph[0][0], 0, 0]]

    # 방향 벡터 정의 (상하좌우 이동)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        currentValue, currentY, currentX = heapq.heappop(heap)

        # 이미 최소 비용이 더 작은 경우에는 처리하지 않음
        if dist[currentY][currentX] < currentValue: continue

        # 상하좌우 인접한 칸 탐색
        for dy, dx in directions:
            moveY = dy + currentY
            moveX = dx + currentX

            # 인접한 칸이 범위 안에 있는지 확인
            if 0 <= moveY < N and 0 <= moveX < N:
                # 현재 칸을 거쳐서 이동했을 때의 비용 계산
                if dist[moveY][moveX] > currentValue + graph[moveY][moveX]:
                    dist[moveY][moveX] = currentValue + graph[moveY][moveX]
                    heapq.heappush(heap, (dist[moveY][moveX], moveY, moveX))

    # 문제 번호 증가
    ProblemCount += 1

    # 문제 번호와 최소 비용 출력
    print(f"Problem {ProblemCount}: {dist[N-1][N-1]}")
