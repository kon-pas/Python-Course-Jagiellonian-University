import random

class RandomQueue:
	def __init__(self, size):
		self.n = 0
		self.size = size
		self.items = [None for x in range(self.size)]

	def insert(self, data):
		if self.is_full() is False:
			self.items[self.n] = data
			self.n += 1

	def remove(self):
		self.n += -1
		r = random.randint(0, self.n)
		value = self.items[r]
		self.items[r] = self.items[self.n]
		self.items[self.n] = None
		return	value

	def is_empty(self):
		return self.n == 0

	def is_full(self):
		return self.size == self.n

	def clear(self):
		self.items = [None for x in range(self.size)]
		self.n = 0
