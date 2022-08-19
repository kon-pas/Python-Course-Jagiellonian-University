class Stack:
	def __init__(self, size):
		self.items = []
		self.size = size
		self.bool = [0 for x in range(size)]

	def __str__(self):
		return str(self.items)

	def is_empty(self):
		return not self.items

	def is_full(self):
		return False

	def push(self, item):
		if item < 0:
			raise IndexError("Podaj liczbe wieksza lub rowna 0")
		elif item > self.size:
			raise IndexError(f"Podaj liczbe mniejsza lub rowna {self.size - 1}")

		if self.bool[item] == 0:
			self.items.append(item)
			self.bool[item] = 1

	def pop(self):
		temp = self.items.pop()
		self.bool[temp] = 0
		return temp
