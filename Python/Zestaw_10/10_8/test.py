import rqueue

if __name__ == "__main__":
	queue = rqueue.RandomQueue(5)

	print("\n1. ", end=" ")
	queue.insert(1)
	queue.insert(7)
	queue.insert(3)
	queue.insert(5)
	queue.insert(8)
	while queue.is_empty() is False:
		print(queue.remove(), end=" ")

	print("\n2. ", end=" ")
	queue.insert(1)
	queue.insert(7)
	queue.insert(3)
	queue.insert(5)
	queue.insert(8)
	while queue.is_empty() is False:
		print(queue.remove(), end=" ")

	print("\n3. ", end=" ")
	queue.insert(1)
	queue.insert(7)
	queue.insert(3)
	queue.insert(5)
	queue.insert(8)
	while queue.is_empty() is False:
		print(queue.remove(), end=" ")
