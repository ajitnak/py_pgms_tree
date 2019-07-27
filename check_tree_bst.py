def check_bst(root, left=None, right=None):
	if not root:
		return True
	if left and root.data < left.data:
		return False
	if right and root.data > right.data:
		return False

	return check_bst(root.left, left, root) and check_bst(root.right, root, right)


