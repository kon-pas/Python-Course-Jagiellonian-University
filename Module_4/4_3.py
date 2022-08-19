def factorial(n):
	result = 1
	for number in range(1, n+1):
		result *= number
	return result

if __name__ == '__main__':
	for i in range(0, 11):
		print(factorial(i))
