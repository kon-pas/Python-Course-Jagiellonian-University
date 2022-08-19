import pqueue as pq

if __name__ == "__main__":
	queue = pq.PriorityQueue()

	for e in [1, 3, 3, 7]:
		queue.insert(e)
	while not queue.is_empty():
		print(queue.remove(), end=" ")

	print("\nIncrease by 1:")
	for e in [1, 3, 3, 7]:
		queue.insert(e)
	queue.increase()
	while not queue.is_empty():
		print(queue.remove(), end=" ")

	print("\nIncrease by 3:")
	for e in [1, 3, 3, 7]:
		queue.insert(e)
	queue.increase(3)
	while not queue.is_empty():
		print(queue.remove(), end=" ")
