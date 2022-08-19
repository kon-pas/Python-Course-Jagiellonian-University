class SingleList:
	"""Klasa reprezentujaca cala liste jednokierunkowa"""

	def __init__(self):
		self.length = 0
		self.head = None
		self.tail = None

	def is_empty(self):
		return self.head is None

	def count(self):
		return self.length

	def insert_head(self, node):
		if self.head:
			node.next = self.head
			self.head = node
		else:
			self.head = self.tail = node
		self.length += 1

	def insert_tail(self, node):
		if self.head:
			self.tail.next = node
			self.tail = node
		else:
			self.head = self.tail = node
		self.length += 1

	def remove_head(self):
		if self.is_empty():
			raise ValueError("Pusta lista")
		node = self.head
		if self.head == self.tail:
			self.head = self.tail = None
		else:
			self.head = self.head.next
		node.next = None
		self.length -= 1
		return node

	def search(self, data):
		node = self.head
		pos = 0
		while node is not None:
			if node.data is data:
				return pos
			node = node.next
			pos += 1
		return None

	def find_min(self):
		node = minimum = self.head
		while node is not None:
			if node.data < minimum.data:
				minimum = node
			node = node.next
		return minimum

	def find_max(self):
		node = maximum = self.head
		while node is not None:
			if node.data > maximum.data:
				maximum = node
			node = node.next
		return maximum

	def reverse(self):
		node = self.head
		prev = None
		while node is not None:
			next = node.next
			node.next = prev
			prev = node
			node = next
		self.head = prev

	def print(self):
		arr = []
		node = self.head
		while node is not None:
			arr.append(node.data)
			node = node.next
		print(arr)
