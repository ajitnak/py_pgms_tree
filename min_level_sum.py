def min_level_sum(root):
	if not root:
		return None
	q = dequeue()
	d = defaultdict(int)

	q.append((0, root))
	while q:
		lvl,n =  q.popleft()
		d[lvl] += n.data
		if  n.left:
			q.append((lvl+1, n.left))
		if n.right:
			q.append((lvl+1, n.right))
	return min(d, key=d.get)


