import sys

input = sys.stdin.readline  
N = int(input())  
data = []  

for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    start = sm * 100 + sd  # 시작 날짜를 숫자로 변환 (예: 3월 1일 -> 301)
    end = em * 100 + ed  # 종료 날짜를 숫자로 변환 (예: 5월 31일 -> 531)
    data.append([start, end]) 

# 피는 날짜(start)를 기준으로 오름차순 정렬
# 같은 시작 날짜일 경우, 지는 날짜(end)를 기준으로 내림차순 정렬
data.sort(key=lambda x: (x[0], -x[1]))

# 목표 구간: 3월 1일(301)부터 11월 30일(1130)까지
startTarget = 301  # 현재 덮어야 할 시작 날짜
endTarget = 1130   # 덮어야 할 종료 날짜
max_end = 0        # 현재 구간에서 가장 멀리 덮을 수 있는 종료 날짜
count = 0          # 선택한 꽃의 개수
idx = 0            # 탐색 인덱스

# 3월 1일부터 11월 30일까지의 구간을 덮기 위해 반복
while startTarget <= endTarget:
	# 현재 구간을 덮을 수 있는 꽃의 최대 종료 날짜를 찾음
	while idx < N and data[idx][0] <= startTarget:
		max_end = max(max_end, data[idx][1])  # 가장 멀리 덮을 수 있는 종료 날짜 갱신
		idx += 1

	# 더 이상 덮을 수 없는 경우
	if max_end <= startTarget:
		print(0)
		exit(0)

	# 꽃을 선택하고 다음 구간으로 이동
	count += 1
	startTarget = max_end

# 모든 구간을 덮었으면 선택한 꽃의 개수 출력
print(count)
