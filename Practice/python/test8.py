import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    # a번 학생이 b번 학생보다 키가 작음을 기록
    graph[a][b] = True

# 플로이드-워셜 알고리즘 적용
# 모든 학생 간의 간접적인 키 비교 관계를 계산
for k in range(1, N+1):  
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True

# 결과 계산
result = 0  
for i in range(1, N + 1):  
    # 자신보다 키가 큰 학생의 수 계산 (i → j 관계인 j의 수)
    bigger_count = sum(graph[i][j] for j in range(1, N + 1))
    # 자신보다 키가 작은 학생의 수 계산 (j → i 관계인 j의 수)
    smaller_count = sum(graph[j][i] for j in range(1, N + 1))

    # 키가 큰 학생 수 + 키가 작은 학생 수 == N - 1인 경우 순서를 알 수 있음
    if bigger_count + smaller_count == N - 1:
        result += 1  # 조건을 만족하는 학생 수 증가

# 최종 결과 출력
print(result)
