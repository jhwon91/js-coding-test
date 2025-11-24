import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = (Y * 100) //X
left = 1
right = X
result = float('inf')

if Z >= 99:
	print(-1)
	exit()


while (left <= right):
	mid = (left + right) //2
	tempZ = ((Y+mid) * 100) //(X+mid)

	if tempZ > Z:
		result = min(result,mid)
		right = mid -1
	else:
		left = mid + 1

print(result)





