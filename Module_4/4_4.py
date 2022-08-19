def fibonacci(n):
	prv, nxt, tmp = 0, 1, 1
	for i in range(n):
		tmp = prv
		prv += nxt
		nxt = tmp
	return prv

if __name__ == '__main__':
	for i in range(0, 21):
		print(fibonacci(i), end=' ')
