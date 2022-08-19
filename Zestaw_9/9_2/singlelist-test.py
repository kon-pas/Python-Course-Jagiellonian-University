import singlelist as sl
import node as n

if __name__ == "__main__":
	alist = sl.SingleList()
	alist.insert_head(n.Node(1))
	alist.insert_tail(n.Node(2))
	alist.insert_head(n.Node(3))
	alist.insert_tail(n.Node(4))
	alist.insert_head(n.Node(5))
	alist.insert_tail(n.Node(6))
	alist.insert_head(n.Node(7))
	alist.insert_tail(n.Node(8))
	alist.insert_head(n.Node(9))
	alist.print()

	# search
	for i in range(alist.count() + 1):
		print(f'{i} is at position: {alist.search(i)}')

	# find_min
	print(f'Minimum: {alist.find_min()}')

	# find_max
	print(f'Maximum: {alist.find_max()}')

	# reverse
	alist.reverse()
	print("Reversed list: ", end='')
	alist.print()
