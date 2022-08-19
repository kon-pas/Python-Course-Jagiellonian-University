import stack

if __name__ == "__main__":
	s = stack.Stack(5)
	s.push(1)
	s.push(0)
	s.push(3)
	s.push(4)
	print(str(s))
	print(s.pop())
	print(str(s))
	s.push(2)
	s.push(2)
	print(str(s))
