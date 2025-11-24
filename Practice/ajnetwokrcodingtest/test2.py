import sys 
input = sys.stdin.readline

INF = float('inf')
N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
	for i in range(N):
		for j in range(N):
			if data[i][k] and data[k][j]:
				data[i][j] = 1

for row in data:
	print(' '.join(map(str,row)))

