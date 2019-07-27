# O(n) algorithm
def count_univals(root): 
	count, _ = count_unival_helper(root)
	return count


def count_univals_helper(root): 
	if not root:
		return 0, True

	luv_cnt, is_luv = count_univals_helper(root.left)
	ruv_cnt, is_ruv = count_univals_helper(root.right)
	uv_cnt = luv_cnt + ruv_cnt
 	if is_luv and is_ruv:
		if root.left and root.value != root.left.value:
			return uv_cnt, False
		if root.right and root.value != root.right.value:
			return uv_cnt, False
		return uv_cnt+1, True

	return uv_cnt, False


#O(n^2 algorithm)
def is_unival(root):
	if not root:
		return True
	if root.left and root.value != root.left.value:
		return False
	if root.right and root.value != root.right.value:
		return False
	if is_unival(root.left) and is_unival(root.right):
		return True
	return False

def count_univals_bad(root):
	if not root:
		return 0
	uv_cnt = count_univals_bad(root.left) + count_univals_bad(root.right)
	if is_unival(root):
		return uv_cnt + 1
	return uv_cnt
	
	
		
