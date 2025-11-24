def main(data):
	answer = 0
	
	for i in range(len(data)):
		for j in range(i+1,len(data)):
			# print(data[i],data[j], checkNum(data[i],data[j]))
			answer += checkNum(data[i],data[j])
	
	return answer 

def checkNum(num1, num2):
	for i in range(max(num1,num2), num1 * num2 + 1):
		if i % num1 == 0 and i % num2 == 0:
			return i
	return num1 * num2

if __name__ == '__main__':
	data = [ 1 , 2 , 3 ]
	print(main(data))


