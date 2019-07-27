class bNode(object):
	def __init__(self, data):
		self.data  = data
		self.left = None
		self.right = None

class bTree:
	def __init__(self)
		self.root = None

	def insert(self, data):
		self.root = self.__insert(root, data)

	def __insert(self, node, data)
		if not node:
			node = bNode(data)
		elif data <= node.data:
			node.left =  self.__insert(self.left, data)
		else 
			node.right = self.__insert(self.right, data)
		return node

	def delete(self, data):
		self.__delete(self, root, data)

	def __delete(self, node, data):
		if not node:
			return
		if data < node.data:
			node.left = __delete(node.left, data)
		elif data > node.data:
			node.right = __delete(node.right, data)
		else:
			if not node.right:
				temp = node.left
				node = None
				return temp
			elif not node.left:
				temp = node.right
				node = None
				return temp
			else:
				temp = min_node(node.right)
				node.data = temp.data
				node.right = self.__delete(node.right, temp.data)
				return node

	def min_node(self):
		if not self.root:
			return None
		node = self.root
		while node.left:
			node = node.left
		return node
