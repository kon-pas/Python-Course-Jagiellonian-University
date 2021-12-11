import node as n
import btree as bt

if __name__ == "__main__":

	root = n.Node()
	root.left = n.Node()
	root.right = n.Node()
	root.left.left = n.Node()
	root.left.right = n.Node()
	root.right.left = n.Node()
	root.right.right = n.Node()
	root.left.left.left = n.Node()
	root.left.left.right = n.Node()

	print("Leaves total:", bt.count_leaves(root))

	root = n.Node(1)
	root.left = n.Node(2)
	root.right = n.Node(3)
	root.left.left = n.Node(4)
	root.left.right = n.Node(5)
	root.right.left = n.Node(6)
	root.right.right = n.Node(7)
	root.left.left.left = n.Node(8)
	root.left.left.right = n.Node(9)

	print("Node values total:", bt.count_total(root))
