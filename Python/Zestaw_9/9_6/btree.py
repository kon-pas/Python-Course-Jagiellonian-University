def count_leaves(top):
	if top.left is None:
		if top.right is None:
			return 1
		else:
			return count_leaves(top.right)
	if top.right is None:
		if top.left is None:
			return 1
		else:
			return count_leaves(top.left)
	else:
		return count_leaves(top.left) + count_leaves(top.right)

def count_total(top):
	if top.left is None:
		if top.right is None:
			return top.data
		else:
			return count_total(top.right) + top.data
	if top.right is None:
		if top.left is None:
			return top.data
		else:
			return count_total(top.left) + top.data
	else:
		return count_total(top.left) + count_total(top.right) + top.data
